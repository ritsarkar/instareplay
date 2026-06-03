# InstaReply AI

InstaReply AI is a production-ready, AI-powered Instagram DM automation platform designed specifically for businesses to handle high-volume inquiries securely and efficiently.

It seamlessly integrates the **Meta Graph API** with **Gemini 2.0 Flash** and a custom **pgvector Knowledge Base**, providing zero-latency asynchronous replies driven by a robust Celery + Redis task queue.

## Features

- **OAuth 2.0 Integration**: Secure login and connection to Instagram Professional accounts.
- **Real-Time Webhooks**: Validates and ingests Meta webhook events (messages) instantaneously.
- **RAG Knowledge Base**: Upload custom documents. The system chunks and embeds them via OpenAI into a PostgreSQL `pgvector` store.
- **Gemini 2.0 Powered**: Semantic vector similarity search combines with conversation history to prompt Gemini 2.0 Flash for highly accurate, contextual answers.
- **Asynchronous Architecture**: Built on FastAPI, Celery, and Redis to handle sudden traffic spikes without dropping Meta webhook callbacks.
- **Premium Dashboard**: A Next.js 15, TailwindCSS, and Lucide React frontend featuring micro-animations, glassmorphism, and live polling for RAG processing status.

## Architecture

```mermaid
graph TD;
    User[User/Customer] -->|DM on Instagram| Meta[Meta Graph API]
    Meta -->|Webhook| FastAPI[FastAPI Backend]
    FastAPI -->|Enqueue Task| Redis[Redis Broker]
    Redis --> Celery[Celery Workers]
    
    Celery -->|1. Search| PgVector[(PostgreSQL pgvector)]
    Celery -->|2. Generate| Gemini[Gemini 2.0 API]
    Celery -->|3. Dispatch| Meta
    
    NextJS[Next.js Dashboard] -->|REST API| FastAPI
```

## Tech Stack
- **Frontend**: Next.js 15 (App Router), React, TailwindCSS, Axios
- **Backend**: FastAPI, Python 3.12, Celery, httpx
- **Database**: PostgreSQL 16 (with pgvector), SQLAlchemy 2.0 (Asyncpg)
- **Cache / Broker**: Redis
- **AI / Embeddings**: Google Gemini 2.0 Flash, OpenAI (text-embedding-3-small)

## Getting Started (Docker Compose)

The easiest way to run the entire stack (Database, Cache, Backend, Frontend, and Workers) is via Docker Compose.

### 1. Environment Variables

Create a `.env` file in the root directory (where `docker-compose.yml` is located) and add the following keys. 

```env
# Database & Cache
DATABASE_URL=postgresql+asyncpg://postgres:postgres@postgres:5432/instareply
UPSTASH_REDIS_URL=redis://redis:6379/0

# Security (Generate random strings for these)
APP_SECRET_KEY=your_random_app_secret
JWT_SECRET_KEY=your_random_jwt_secret
FERNET_KEY=your_base64_fernet_key # Must be exactly 32 url-safe base64-encoded bytes

# Meta Configuration
META_APP_ID=your_meta_app_id
META_APP_SECRET=your_meta_app_secret
META_WEBHOOK_VERIFY_TOKEN=your_custom_verify_token
META_API_VERSION=v21.0

# AI APIs
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key

# Frontend
FRONTEND_URL=http://localhost:3000
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 2. Run the Stack

Execute the following command in the root directory:

```bash
docker-compose up -d --build
```

This will spin up:
- `postgres` on port `5432`
- `redis` on port `6379`
- `backend` (FastAPI) on port `8000`
- `frontend` (Next.js) on port `3000`
- `worker` (Celery worker)

### 3. Access the Application

- **Dashboard**: Navigate to `http://localhost:3000`
- **API Docs**: Navigate to `http://localhost:8000/docs`

## Security Notes
- Tokens are encrypted at rest using symmetric `Fernet` encryption before being stored in PostgreSQL.
- API endpoints are protected using HttpOnly cookies to prevent XSS attacks against JWT tokens.
- All webhook payloads are cryptographically verified using `HMAC SHA-256` matching against the `META_APP_SECRET`.
