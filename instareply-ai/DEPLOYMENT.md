# InstaReply AI - Firebase Deployment Guide

This guide will walk you through deploying your local Docker application to **Google Firebase** and **Google Cloud Run**.

---

## 1. Prepare Your Databases
Firebase offers NoSQL (Firestore), but our AI Knowledge Base requires PostgreSQL with the `pgvector` extension. We will use free third-party providers for our databases.

1. **PostgreSQL (Supabase)**: Create a free [Supabase](https://supabase.com/) project. Copy the Connection String (replace `postgresql://` with `postgresql+asyncpg://`). Run `docker-compose run backend alembic upgrade head` locally with this new URI to create your tables on the live database.
2. **Redis (Upstash)**: Create a free [Upstash](https://upstash.com/) Redis database. Copy the `rediss://...` URL. This will power the Celery worker queue.

---

## 2. Deploy the Backend (Google Cloud Run)
Your backend is built with FastAPI and runs inside a Docker container. We will deploy this container to Google Cloud Run, which integrates perfectly with Firebase.

1. Install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).
2. Authenticate and set your project:
   ```bash
   gcloud auth login
   gcloud config set project [YOUR_FIREBASE_PROJECT_ID]
   ```
3. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
4. Build and deploy to Cloud Run:
   ```bash
   gcloud run deploy instareply-ai-backend \
     --source . \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars="APP_ENV=production,DATABASE_URL=[YOUR_SUPABASE_URL],UPSTASH_REDIS_URL=[YOUR_UPSTASH_URL],..." 
   ```
5. *(Optional but required for production)*: Deploy a second Cloud Run service named `instareply-ai-worker` using a custom command to run Celery instead of FastAPI.

---

## 3. Deploy the Frontend (Firebase Hosting)
Firebase Hosting has native support for Next.js (WebFrameworks). We have already prepared the `firebase.json` file to route `/api/*` requests automatically to your Cloud Run backend!

1. Install the Firebase CLI:
   ```bash
   npm install -g firebase-tools
   ```
2. Log into Firebase:
   ```bash
   firebase login
   ```
3. Link your local directory to your Firebase project:
   ```bash
   firebase use [YOUR_FIREBASE_PROJECT_ID]
   ```
4. Deploy the frontend:
   ```bash
   firebase deploy --only hosting
   ```
   *Firebase will automatically detect your Next.js app in the `frontend` folder, build it, and deploy it to your `.web.app` domain.*

---

## 4. Final Meta Webhook Update
Now that your application is live, you must tell Instagram where to send messages.

1. Go to the [Meta Developer Portal](https://developers.facebook.com/).
2. Navigate to your App -> **Messenger** -> **Instagram Settings**.
3. Edit your Webhook URL to point to your new live backend. Since Firebase Rewrites are active, use your Firebase domain:
   - `https://[YOUR_PROJECT_ID].web.app/api/webhooks/meta`
4. Enter your `META_WEBHOOK_VERIFY_TOKEN` and click Verify.

**Congratulations! Your SaaS is now live on Google Firebase!**
