#!/usr/bin/node
/*
Return the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
*/

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let h = 0; h < list.length; h++) {
    if (list[h] === searchElement) {
      count++;
    }
  }
  return count;
};
