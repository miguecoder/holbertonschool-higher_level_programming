#!/usr/bin/node
const array = process.argv;
if (parseInt(array[2])) {
  for (let i = 0; i < array[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
