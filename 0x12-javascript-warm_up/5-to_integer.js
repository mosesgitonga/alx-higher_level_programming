#!/usr/bin/node

const val = process.argv[2];
const parsedval = parseInt(val);

if (process.argv[2] === undefined || isNaN(parsedval)) {
  console.log('Not a number');
} else {
  console.log('My number: ', parsedval);
}
