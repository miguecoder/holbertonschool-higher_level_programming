#!/usr/bin/node
const array = process.argv;
const x = parseInt(array[2]);
const y = parseInt(array[3]);
function add (a, b) {
  console.log(a + b);
}
add(x, y);
