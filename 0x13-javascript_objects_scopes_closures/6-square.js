#!/usr/bin/node

const Mysquare = require('./5-square');

class Square extends Mysquare {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
      }

    for (let i = 1; i <= this.height; i++) {
      console.log(c.repeat(this.height));

    }
   }
  }


module.exports = Square;
