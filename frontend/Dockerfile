# --- build : compile l'application Angular ---
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build -- --configuration production

# --- run : nginx sert le build et relaie /api vers le backend ---
FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/tuteur/browser /usr/share/nginx/html
