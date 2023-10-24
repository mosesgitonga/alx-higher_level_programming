#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const baseURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(baseURL, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
