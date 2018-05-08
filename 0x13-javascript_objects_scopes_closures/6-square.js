#!/usr/bin/node
const inheritSquare = require('./5-square.js');
class Square extends inheritSquare {
  charPrint (c) {
    if (c === undefined) {
      for (let index = 0; index < this.height; index++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
