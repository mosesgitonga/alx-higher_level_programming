#!/usr/bin/node
const fs = require('fs');
const arg = process.argv.slice(2);
const filename = arg[0];
const filepath = `./${filename}`;

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
