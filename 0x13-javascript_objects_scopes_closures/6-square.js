#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
  charPrint (c) {
    if (c === undefined) {
      for (let index = 0; index < this.size; index++) {
        console.log('X'.repeat(this.size));
      }
    } else {
      for (let index = 0; index < this.size; index++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
