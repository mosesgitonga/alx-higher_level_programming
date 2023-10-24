#!/usr/bin/node
const request = require('request');
const charID = '18';
const url = process.argv[2];
let numFilms = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  data.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(charID)) {
        numFilms += 1;
      }
    });
  });
  console.log(numFilms);
});
