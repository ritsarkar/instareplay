"""Billing routes for Razorpay subscriptions."""

import razorpay
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.config import settings
from app.database import get_db
from app.routers.auth import get_current_user
from app.models.user import User
from app.models.subscription import Subscription
from app.models.enums import Plan, SubscriptionStatus

# Initialize Razorpay Client if keys are present
client = None
if settings.razorpay_key_id and settings.razorpay_key_secret:
    client = razorpay.Client(auth=(settings.razorpay_key_id, settings.razorpay_key_secret))

router = APIRouter(prefix="/billing", tags=["billing"])

class RazorpayVerifyRequest(BaseModel):
    razorpay_payment_id: str
    razorpay_order_id: str
    razorpay_signature: str

@router.post("/create-razorpay-order")
async def create_razorpay_order(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Generate a Razorpay Order ID for the Pro plan."""
    
    # Mock mode for testing without real Razorpay keys
    if not client:
        stmt = select(Subscription).where(Subscription.user_id == current_user.id)
        result = await db.execute(stmt)
        subscription = result.scalars().first()
        
        if subscription:
            subscription.plan = Plan.PRO
            subscription.status = SubscriptionStatus.ACTIVE
        else:
            new_sub = Subscription(
                user_id=current_user.id,
                plan=Plan.PRO,
                status=SubscriptionStatus.ACTIVE
            )
            db.add(new_sub)
        await db.commit()
        return {"mock": True, "message": "Mock mode: Account upgraded instantly."}

    # Real Razorpay Order Creation
    AMOUNT = 4900 # $49.00 -> Razorpay expects paise (INR) or cents, let's assume 4900 INR for Indian Gateway
    
    try:
        data = {
            "amount": AMOUNT * 100, # amount in smallest currency unit
            "currency": "INR",
            "receipt": str(current_user.id),
            "notes": {
                "user_email": current_user.email
            }
        }
        order = client.order.create(data=data)
        return {
            "mock": False,
            "order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key_id": settings.razorpay_key_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/razorpay-verify")
async def verify_razorpay_signature(
    request_data: RazorpayVerifyRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Verify the Razorpay payment signature and update subscription."""
    
    if not client:
        return {"status": "success", "message": "Mock mode: Verified."}

    try:
        # Verify the signature
        client.utility.verify_payment_signature({
            'razorpay_order_id': request_data.razorpay_order_id,
            'razorpay_payment_id': request_data.razorpay_payment_id,
            'razorpay_signature': request_data.razorpay_signature
        })
        
        # Payment is verified, update the subscription in DB
        stmt = select(Subscription).where(Subscription.user_id == current_user.id)
        result = await db.execute(stmt)
        subscription = result.scalars().first()
        
        if subscription:
            subscription.razorpay_subscription_id = request_data.razorpay_order_id # Using order ID as reference
            subscription.plan = Plan.PRO
            subscription.status = SubscriptionStatus.ACTIVE
        else:
            new_sub = Subscription(
                user_id=current_user.id,
                razorpay_subscription_id=request_data.razorpay_order_id,
                plan=Plan.PRO,
                status=SubscriptionStatus.ACTIVE
            )
            db.add(new_sub)
            
        await db.commit()
        return {"status": "success"}

    except razorpay.errors.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Signature Verification Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
