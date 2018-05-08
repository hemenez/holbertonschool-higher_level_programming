#!/usr/bin/node
const inheritSquare = require('./5-square.js');
class Square extends inheritSquare {
  charPrint (c) {
    console.log(inheritSquare.size);
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
