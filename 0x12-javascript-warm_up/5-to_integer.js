#!/usr/bin/node
const array = process.argv;
if (parseInt(array[2])) {
  console.log('My number: ' + parseInt(array[2]));
} else {
  console.log('Not a number');
}
