#!/usr/bin/node
const args = process.argv;
const lenArgs = args.length;

if (lenArgs <= 3) {
  console.log(0);
} else {
  const list = args.sort();
  const res = list.reverse()[1];
  console.log(res);
}
