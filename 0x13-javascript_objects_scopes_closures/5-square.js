#!/usr/bin/node

// Import the Rectangle class
const Rect = require('./4-rectangle');

// Class name Sq inherits from Rectangle
class Sq extends Rect {
  constructor (s) {
    // Call the constructor with width and height set to 's'
    super(s, s);
  }
}

// Export the Square class for use in other modules
module.exports = Sq;
