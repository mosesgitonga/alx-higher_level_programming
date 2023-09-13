#!/usr/bin/node
const data = require('./100-data').list;

const multipliedByIndex = data.map((value, index) => {
  return value * index;
});

console.log(data);
console.log(multipliedByIndex);
