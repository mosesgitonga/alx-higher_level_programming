#!/usr/bin/node
const args = process.argv;
const lenArgs = args.length - 2;
let biggest = Number.NEGATIVE_INFINITY;

if (lenArgs <= 2) {
  console.log(0);
} else {
  for (let i = 2; i <= lenArgs + 1; i++) {
    const currNumber = parseFloat(args[i]);
    if (!isNaN(currNumber) && currNumber > biggest) {
      biggest = currNumber;
    }
  }
}
if (biggest !== Number.NEGATIVE_INFINITY) {
  console.log(biggest);
}
