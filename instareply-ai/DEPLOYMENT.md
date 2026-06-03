# InstaReply AI - Production Deployment Guide

This guide will walk you through moving your local Docker application to the live internet for free (or extremely cheap) using modern serverless platforms.

---

## 1. Prepare Your Repository
Before deploying, ensure all your code is pushed to a Git repository (like GitHub).
```bash
git add .
git commit -m "Ready for production deployment"
git push origin main
```

---

## 2. Set Up the Database (Supabase)
We need a live PostgreSQL database that supports the `pgvector` extension for our RAG AI.

1. Go to [Supabase](https://supabase.com/) and create a free account.
2. Create a new Project.
3. Once the database is provisioned, go to **Project Settings** -> **Database**.
4. Copy the **Connection String (URI)**. It should look like `postgresql://postgres.[PROJECT_ID]:[PASSWORD]@aws-0-us-west-1.pooler.supabase.com:6543/postgres`.
5. *Important*: Replace `postgresql://` with `postgresql+asyncpg://` so our Python backend can communicate with it asynchronously.
6. Run your Alembic migrations against this live database (from your local machine, temporarily set your local `.env` DATABASE_URL to this live URI, and run `docker-compose run backend alembic upgrade head`).

---

## 3. Set Up Redis (Upstash)
We need a live Redis instance to handle our Celery background tasks (the workers that process webhooks asynchronously).

1. Go to [Upstash](https://upstash.com/) and create a free account.
2. Click **Create Database** under the Redis section.
3. Scroll down to the **Connect** section and select "Python" or "URL".
4. Copy the `rediss://...` URL.

---

## 4. Deploy the Backend (Render.com)
We have already created a `render.yaml` file in the root of the repository to automate this!

1. Go to [Render](https://render.com/) and sign in with your GitHub account.
2. Go to your Dashboard, click **New +**, and select **Blueprint**.
3. Connect your GitHub repository.
4. Render will automatically detect the `render.yaml` file and prepare to deploy **two** services:
   - Your FastAPI Web Service
   - Your Celery Background Worker
5. Click **Apply**.
6. Render will ask you to fill in the missing environment variables (e.g. `DATABASE_URL`, `UPSTASH_REDIS_URL`, `OPENAI_API_KEY`, `RAZORPAY_KEY_ID`, etc.).
7. Once deployed, copy the **Backend URL** (e.g. `https://instareply-ai-backend.onrender.com`).

*Note: If your backend URL is different from `instareply-ai-backend.onrender.com`, you must update the `destination` URL in the `frontend/vercel.json` file in your repository!*

---

## 5. Deploy the Frontend (Vercel)
Vercel is the creator of Next.js and provides the best hosting experience for the frontend.

1. Go to [Vercel](https://vercel.com/) and sign in with GitHub.
2. Click **Add New** -> **Project**.
3. Import your GitHub repository.
4. Under **Framework Preset**, ensure it says `Next.js`.
5. Under **Root Directory**, click Edit and select the `frontend` folder.
6. Add your environment variables:
   - `NEXT_PUBLIC_API_URL` = `/api` (This works because of our `vercel.json` rewrites)
7. Click **Deploy**.

---

## 6. Final Meta Webhook Update
Now that your backend is live on the internet, you no longer need `ngrok`!

1. Go to the [Meta Developer Portal](https://developers.facebook.com/).
2. Navigate to your App -> **Messenger** -> **Instagram Settings**.
3. Edit your Webhook URL to point to your new live backend:
   - `https://instareply-ai-backend.onrender.com/api/webhooks/meta`
4. Enter your `META_WEBHOOK_VERIFY_TOKEN` and click Verify.

**Congratulations! Your AI SaaS is now live on the internet and ready to accept real payments and Instagram messages!**
