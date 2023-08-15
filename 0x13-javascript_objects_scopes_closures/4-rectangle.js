#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || w <= 0) {
      console.log('Rectangle {}');
    } else if (typeof h !== 'number' || h <= 0) {
      console.log('Rectangle {}');
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let line = '';
      for (let y = 0; y < this.width; y++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
