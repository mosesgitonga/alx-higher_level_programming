#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    if (this.height && this.width) {
      for (let i = 1; i <= this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.height && this.width) {
      const temp = this.height;
      this.height = this.width;
      this.width = temp;
    }
  }

  double () {
    if (this.height && this.width) {
      this.height = this.height * 2;
      this.width = this.width * 2;
    }
  }
}

module.exports = Rectangle;
