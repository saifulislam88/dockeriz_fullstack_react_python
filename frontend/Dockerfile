FROM node:16 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:latest AS prod
COPY --from=build /app/build /usr/share/nginx/html
