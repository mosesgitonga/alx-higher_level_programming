#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x) || x <= 0) {
  return;
} else {
  for (let i = 0; i < x; i++) {
	let line = '';
	for (let j = 0; j < x; j++) {
	  line += 'x';
	}
	console.log(line);
  }
}
