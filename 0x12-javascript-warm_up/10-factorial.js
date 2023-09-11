#!/usr/bin/node

function factorial (target) {
  if (target === 0 || target === 1) {
    return 1;
  } else {
    return target * factorial(target - 1);
  }
}
const target = parseInt(process.argv[2]);
if (!isNaN(target)) {
  const res = factorial(target);
  console.log(res);
} else {
  console.log('1');
}
