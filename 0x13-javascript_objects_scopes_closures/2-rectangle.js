#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (typeof width !== 'number' || width <= 0) {
      return 'Rectangle {}';
    } else if (typeof height !== 'number' || height <= 0) {
      return 'Rectangle {}';
    } else {
      this.width = width;
      this.height = height;
    }
  }
}

module.exports = Rectangle;
