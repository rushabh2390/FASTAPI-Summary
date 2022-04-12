#Docker file for VueJS using NGINX
# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install -g npm@8.6.0
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
RUN apk add nano && apk add curl
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
