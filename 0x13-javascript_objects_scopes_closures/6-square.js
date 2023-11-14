#!/usr/bin/node
const squareR = require('./5-square');

class Square extends squareR {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += c;
      }
      console.log(result);
    }
  }
}
module.exports = Square;
