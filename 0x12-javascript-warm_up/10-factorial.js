#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    const res = num * factorial(num - 1);
    return res;
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
