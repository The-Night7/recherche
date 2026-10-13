# Image unique (ex. un seul service Render) : le backend sert l'API et le build Angular.
# Pour deux conteneurs séparés (nginx + backend), voir docker-compose.yml.

# --- 1. build du frontend ---
FROM node:22-alpine AS frontend
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build -- --configuration production

# --- 2. backend + build servi par server.py ---
FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends poppler-utils && rm -rf /var/lib/apt/lists/*
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .
COPY --from=frontend /app/dist/tuteur/browser /app/web
# Render fixe PORT ; server.py l'écoute déjà (voir backend/server.py)
ENV WEB_DIR=/app/web PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "server.py"]
