#!/usr/bin/node

const arg = process.argv;
const num = parseInt(arg[2]);

if (!isNaN(num) && num >= 0) {
  for (let i = 1; i <= num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
