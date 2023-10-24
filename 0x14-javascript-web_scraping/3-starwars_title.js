#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const base_url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(base_url, (err, response, body) => {
    if (err) {
        console.log(err);
    }
    const data = JSON.parse(body);
    console.log(data.title);
});
