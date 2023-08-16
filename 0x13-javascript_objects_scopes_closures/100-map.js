#!/usr/bin/node

const list = require('./100-data.js').list;
const multiplyByIndex = (element, index) => {
  return element * index;
};

const newList = Array.prototype.map.call(list, multiplyByIndex);

console.log(list);
console.log(newList);
