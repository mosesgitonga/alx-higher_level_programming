#!/usr/bin/node

const arg = process.argv;
const num = arg[2];

if (num >= 0) {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
