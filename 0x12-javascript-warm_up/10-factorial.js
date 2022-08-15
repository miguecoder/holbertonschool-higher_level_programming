#!/usr/bin/node
const array = process.argv;
const x = parseInt(array[2]);
function factorial (x) {
  if (isNaN(x) || x < 2) {
    return 1;
  }
  return x * factorial(x - 1);
}
console.log(factorial(x));
