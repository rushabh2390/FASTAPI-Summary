#Docker file for VueJS using NGINX
# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*
COPY . .
# ARG VUE_APP_API_BACKEND=$VUE_APP_API_BACKEND
# ARG VUE_APP_TITLE=$VUE_APP_TITLE
# ENV VUE_APP_TITLE="Fast Api Summary Generator"
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
