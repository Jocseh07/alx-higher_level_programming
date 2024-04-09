#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let a = 0; a < this.height; a++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
