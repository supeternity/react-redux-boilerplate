FROM node:9.11.1

# RUN npm install

# RUN npm install --global nodemon
RUN npm install --quiet --global vue-cli

RUN mkdir -p /frontend

COPY ./package.json /frontend/package.json

WORKDIR /frontend

RUN npm install --quiet
RUN npm i
