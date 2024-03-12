#!/usr/bin/node
function add(a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);
  if (isNaN(numA) || isNaN(numB)) {
    return NaN;
  }
  return numA + numB;
}
console.log(add(process.argv[2], process.argv[3]));
