# BUILD DEPEN
FROM node:18-alpine as build

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

# RUNTIME IMAGE
FROM node:18-alpine

WORKDIR /app

COPY --from=build /app .

EXPOSE 3000

CMD [ "npm" ,"start"]
