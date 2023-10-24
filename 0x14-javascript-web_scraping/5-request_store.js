#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(filepath, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
