#!/usr/bin/node

const args = process.argv;
const argsLen = args.length - 1;

if (argsLen === 2) {
  const num = Number(args[2]);
  if (!isNaN(num)) {
    const floatNum = Math.floor(num);
    console.log(`My number: ${floatNum}`);
  } else {
    console.log('Not a number');
  }
}
