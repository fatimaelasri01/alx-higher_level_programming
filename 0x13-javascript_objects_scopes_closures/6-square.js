#!/usr/bin/node
const squareRef = require('./5-square');

class Square extends squareRef {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let square = '';
        for (let j = 0; j < this.width; j++) {
          square += c;
        }
        console.log(square);
      }
    }
  }
}

module.exports = Square;
