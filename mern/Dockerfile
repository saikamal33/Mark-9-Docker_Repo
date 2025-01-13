##build stage
FROM node:18.9.1 AS build

WORKDIR /app

COPY /front/package.json ./frontend/package.json

COPY /back/package.json ./backend/package.json

RUN npm install --prefix ./frontend
RUN npm install --prefix ./backend

###front end

FROM node:18.9.1 AS front

WORKDIR /app/frontend

COPY --from=build /app/frontend ./frontend

COPY /frontend /app/frontend

EXPOSE 5173

CMD ["npm","run","dev"]

##back end
FROM node:18.9.1 AS back

WORKDIR /app/backend

COPY --from=build /app/backend ./backend

COPY /backend /app/backend

EXPOSE 5050

CMD ["npm","start"]

