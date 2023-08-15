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
    if (this.height && this.width) {
      for (let y = 0; y < this.height; y++) {
        let line = '';
        for (let x = 0; x < this.width; x++) {
          line += 'X';
        }
        console.log(line);
      }
    }
  }
}

module.exports = Rectangle;
