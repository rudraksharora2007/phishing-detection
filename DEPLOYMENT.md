# Deployment Guide

## Local with Docker
1. Copy `backend/.env.example` to `backend/.env` and set secrets.
2. Run:
   - `docker compose up --build`
3. Access:
   - Frontend: `http://localhost:5173`
   - Backend: `http://localhost:5000`

## Manual Local
Backend:
1. `cd backend`
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python ml/train_model.py`
5. `python app.py`

Frontend:
1. `cd frontend`
2. `npm install`
3. `npm run dev`

## Cloud Notes
- Deploy backend to Render/Fly/AWS ECS with env vars.
- Deploy frontend to Vercel/Netlify with `VITE_API_URL`.
- Use managed MongoDB Atlas and enforce IP allowlist.
