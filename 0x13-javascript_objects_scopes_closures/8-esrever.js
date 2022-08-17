#!/usr/bin/node
exports.esrever = function (item) {
  const array = [];
  for (let i = item.length - 1; i >= 0; i--) {
    array.push(item[i]);
  }
  return array;
};
