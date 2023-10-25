#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(body);
    const title = jsonObject.title;
    console.log(title);
  }
});
