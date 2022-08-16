#!/usr/bin/node
exports.addMeMaybe = function (number, theFuntion) {
  number += 1;
  theFuntion(number);
};
