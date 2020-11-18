FROM node:12.18.2 as build

ARG REACT_APP_SERVICES_HOST=/services/m

WORKDIR /app

# Copies Dependencies
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json

# Installs all node packages
RUN npm install

COPY . .

RUN npm run build

FROM nginx:latest
COPY ./nginx/nginx.config /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html