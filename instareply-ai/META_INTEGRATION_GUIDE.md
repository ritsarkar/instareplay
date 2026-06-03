# Meta (Instagram) Integration Guide

To connect InstaReply AI to your Instagram account, you must configure a Meta Developer App and set up webhooks so Meta can send incoming DMs to your backend.

## Step 1: Create a Meta App
1. Go to the [Meta for Developers](https://developers.facebook.com/) portal and log in.
2. Click **My Apps** -> **Create App**.
3. Select **Other** as the use case, then choose **Business**.
4. Name your app (e.g., "InstaReply AI") and provide your contact email.

## Step 2: Add Required Products
On your App Dashboard, scroll down and add the following products:
1. **Instagram Graph API**: This allows you to read and reply to DMs.
2. **Facebook Login for Business**: This is required for the OAuth flow so your users can securely connect their Instagram pages to your SaaS.

## Step 3: Configure Facebook Login
1. Navigate to **Facebook Login for Business** > **Settings** in the left sidebar.
2. Ensure **Valid OAuth Redirect URIs** contains your backend OAuth callback URL.
   - For local development: `http://localhost:8000/api/auth/meta/callback`
   - For production: `https://your-domain.com/api/auth/meta/callback`
3. Save changes.

## Step 4: Obtain App Credentials
1. Go to **App Settings** > **Basic** in the left sidebar.
2. Copy the **App ID** and **App Secret**.
3. Paste these into your `.env` file:
   ```env
   META_APP_ID=your_app_id_here
   META_APP_SECRET=your_app_secret_here
   ```

## Step 5: Configure the Webhook
Meta needs a public HTTPS URL to send incoming Instagram DMs to. Since your backend is running locally on `localhost:8000`, you must use a tunneling service like [ngrok](https://ngrok.com/) to expose it.

1. **Start ngrok** in a new terminal:
   ```bash
   ngrok http 8000
   ```
2. Copy the secure Forwarding URL (e.g., `https://abc-123.ngrok-free.app`).
3. In the Meta Developer Portal, go to **Messenger** > **Instagram Settings**.
4. Under the **Webhooks** section, click **Add Callback URL**.
5. Fill in the fields:
   - **Callback URL**: `https://abc-123.ngrok-free.app/api/webhooks/meta`
   - **Verify Token**: Create a random string (e.g., `my_super_secret_token_123`).
6. Click **Verify and Save**. (Your local Docker backend must be running for Meta to verify it).
7. Paste that exact Verify Token into your `.env` file:
   ```env
   META_WEBHOOK_VERIFY_TOKEN=my_super_secret_token_123
   ```
8. Finally, click **Manage** next to your Webhook and subscribe to the `messages` field.

## Step 6: Restart the Backend
Now that your `.env` is updated with the real Meta credentials, restart your Docker containers so the backend picks up the new secrets:

```bash
docker-compose down
docker-compose up -d
```

Your integration is now fully configured! When you DM your connected Instagram Professional account, Meta will send the payload to your ngrok URL, which forwards to your FastAPI backend, triggering the AI response.
