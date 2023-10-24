#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request.get(character, (err, response, body) => {
      if (err) {
        console.log(err);
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
