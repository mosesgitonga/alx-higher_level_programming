#!/usr/bin/node

function add (a, b) {
  const res = a + b;
  return res;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
console.log(add(a, b));
