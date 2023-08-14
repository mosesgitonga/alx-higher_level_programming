#!/usr/bin/node

const len = process.argv.length;
let biggest = 0;
for (let i = 2; i < len; i++) {
  const num = parseInt(process.argv[i]);
  if (biggest < num && !isNaN(num)) {
    biggest = num;
  }
}
console.log(biggest);
