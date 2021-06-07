#!/usr/bin/node
/*
Func that returns reversed version of list
prototype exports.esrever = function (list)
cannot use reverse
*/

exports.esrever = function (list) {
  const rvrs = [];

  for (let h = list.length - 1; h >= 0; h--) {
    rvrs.push(list[h]);
  }
  return rvrs;
};
