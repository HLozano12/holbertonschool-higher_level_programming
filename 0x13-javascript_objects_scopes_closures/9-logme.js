#!/usr/bin/node
/*
print the # of args already printed
new args value
*/

let count = 0;
exports.logMe = function (item) {
  console.log('%i: %s', count, item);
  /* like Printf */
  count++;
};
