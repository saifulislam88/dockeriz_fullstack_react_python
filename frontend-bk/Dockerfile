FROM node:16 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine AS prod
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
