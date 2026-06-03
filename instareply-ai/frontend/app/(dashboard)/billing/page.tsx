"use client";

import { useState } from "react";
import api from "@/lib/api";
import { Check, Zap, Shield, Sparkles } from "lucide-react";
import Script from "next/script";

// Add Razorpay types to window
declare global {
  interface Window {
    Razorpay: any;
  }
}

export default function BillingPage() {
  const [loading, setLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  const handleUpgrade = async () => {
    setLoading(true);
    try {
      // 1. Create Order on Backend
      const response = await api.post("/api/billing/create-razorpay-order");
      
      const data = response.data;

      // Check if we are in Mock Mode (no keys in .env)
      if (data.mock) {
        setIsSuccess(true);
        setLoading(false);
        return;
      }

      // 2. Initialize Razorpay Options
      const options = {
        key: data.key_id, 
        amount: data.amount,
        currency: data.currency,
        name: "InstaReply AI",
        description: "Upgrade to Pro Plan",
        image: "https://your-logo-url.com/logo.png", // Replace with actual logo
        order_id: data.order_id, 
        handler: async function (response: any) {
          // 3. Verify Payment Signature on Backend
          try {
            const verifyRes = await api.post("/api/billing/razorpay-verify", {
              razorpay_payment_id: response.razorpay_payment_id,
              razorpay_order_id: response.razorpay_order_id,
              razorpay_signature: response.razorpay_signature
            });
            
            if (verifyRes.data.status === "success") {
              setIsSuccess(true);
            }
          } catch (error) {
            console.error("Signature verification failed", error);
            alert("Payment verification failed. Please contact support.");
          }
        },
        prefill: {
          name: "User",
          email: "user@example.com",
        },
        theme: {
          color: "#6366f1", // Indigo 500
        },
      };

      // 4. Open Razorpay Checkout Modal
      const rzp1 = new window.Razorpay(options);
      rzp1.on('payment.failed', function (response: any){
        alert("Payment Failed: " + response.error.description);
      });
      rzp1.open();

    } catch (error) {
      console.error("Failed to initiate checkout:", error);
      alert("Failed to create order. Is the backend running?");
    } finally {
      setLoading(false);
    }
  };

  if (isSuccess) {
    return (
      <div className="flex flex-col items-center justify-center space-y-6 max-w-2xl mx-auto mt-20 text-center">
        <div className="h-20 w-20 bg-emerald-500/20 text-emerald-400 rounded-full flex items-center justify-center">
          <Check className="h-10 w-10" />
        </div>
        <h1 className="text-3xl font-bold text-white">Welcome to Pro!</h1>
        <p className="text-indigo-200">Your payment was successful and your account has been upgraded.</p>
        <button 
          onClick={() => window.location.href = '/dashboard'}
          className="mt-8 px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg transition-colors font-medium"
        >
          Return to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-8 max-w-5xl mx-auto">
      {/* Razorpay SDK */}
      <Script src="https://checkout.razorpay.com/v1/checkout.js" strategy="lazyOnload" />

      <div className="text-center space-y-4">
        <h1 className="text-4xl font-extrabold tracking-tight text-white sm:text-5xl">
          Upgrade your <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">InstaReply</span>
        </h1>
        <p className="text-lg text-indigo-200/70 max-w-2xl mx-auto">
          Scale your business with advanced AI capabilities, unlimited knowledge base documents, and priority support.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12">
        {/* Free Tier */}
        <div className="relative rounded-2xl border border-white/10 bg-white/5 p-8 backdrop-blur-md flex flex-col">
          <div className="mb-6">
            <h3 className="text-xl font-semibold text-white">Starter Plan</h3>
            <p className="text-indigo-200/60 text-sm mt-2">Perfect for trying out InstaReply AI.</p>
          </div>
          <div className="mb-6">
            <span className="text-4xl font-bold text-white">₹0</span>
            <span className="text-indigo-200/60">/month</span>
          </div>
          <ul className="space-y-4 mb-8 flex-1">
            <li className="flex items-center gap-3 text-indigo-100">
              <Check className="h-5 w-5 text-emerald-400" />
              <span>Up to 100 AI Replies / mo</span>
            </li>
            <li className="flex items-center gap-3 text-indigo-100">
              <Check className="h-5 w-5 text-emerald-400" />
              <span>1 Knowledge Document</span>
            </li>
            <li className="flex items-center gap-3 text-indigo-100">
              <Check className="h-5 w-5 text-emerald-400" />
              <span>Basic Support</span>
            </li>
          </ul>
          <button disabled className="w-full py-3 px-4 rounded-lg bg-white/5 text-indigo-200/50 font-medium border border-white/5 cursor-not-allowed">
            Current Plan
          </button>
        </div>

        {/* Pro Tier */}
        <div className="relative rounded-2xl border border-indigo-500/50 bg-indigo-900/20 p-8 backdrop-blur-md flex flex-col shadow-2xl shadow-indigo-500/10">
          <div className="absolute -top-4 inset-x-0 flex justify-center">
            <span className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wide flex items-center gap-1">
              <Sparkles className="h-3 w-3" /> Most Popular
            </span>
          </div>
          
          <div className="mb-6">
            <h3 className="text-xl font-semibold text-white">Pro Plan</h3>
            <p className="text-indigo-200/60 text-sm mt-2">For growing brands that need more power.</p>
          </div>
          <div className="mb-6">
            <span className="text-4xl font-bold text-white">₹4900</span>
            <span className="text-indigo-200/60">/month</span>
          </div>
          <ul className="space-y-4 mb-8 flex-1">
            <li className="flex items-center gap-3 text-indigo-100">
              <Zap className="h-5 w-5 text-indigo-400" />
              <span>Unlimited AI Replies</span>
            </li>
            <li className="flex items-center gap-3 text-indigo-100">
              <Database className="h-5 w-5 text-indigo-400" />
              <span>Unlimited Knowledge Base</span>
            </li>
            <li className="flex items-center gap-3 text-indigo-100">
              <Shield className="h-5 w-5 text-indigo-400" />
              <span>Priority 24/7 Support</span>
            </li>
            <li className="flex items-center gap-3 text-indigo-100">
              <Check className="h-5 w-5 text-emerald-400" />
              <span>Custom System Prompts</span>
            </li>
          </ul>
          <button 
            onClick={handleUpgrade}
            disabled={loading}
            className="w-full py-3 px-4 rounded-lg bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-medium hover:from-indigo-600 hover:to-purple-700 transition-all flex justify-center items-center gap-2"
          >
            {loading ? (
              <span className="animate-spin h-5 w-5 border-2 border-white border-t-transparent rounded-full"></span>
            ) : (
              "Upgrade to Pro with Razorpay"
            )}
          </button>
        </div>
      </div>
    </div>
  );
}

// Inline placeholder for Database icon
function Database(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <ellipse cx="12" cy="5" rx="9" ry="3" />
      <path d="M3 5V19A9 3 0 0 0 21 19V5" />
      <path d="M3 12A9 3 0 0 0 21 12" />
    </svg>
  )
}
