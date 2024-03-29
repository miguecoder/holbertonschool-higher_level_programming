#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
