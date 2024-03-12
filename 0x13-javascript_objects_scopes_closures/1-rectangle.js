#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If width or height is not positive, return an empty object
      return {};
    } else {
      // Initialize instance attributes
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
