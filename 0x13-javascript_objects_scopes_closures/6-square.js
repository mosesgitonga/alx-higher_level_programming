#!/usr/bin/node
const preSquare = require('./5-square.js');

class Square extends preSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += c;
      }
      console.log(line);
    }
  }
}
module.exports = Square;
