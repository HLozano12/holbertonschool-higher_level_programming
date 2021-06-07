#!/usr/bin/node
/*
convert a # from base 10 to another pass
pass as an argument
prototype used: exports.converter = function (base)
*/

exports.converter = function (base) {
  function baseConverter (numb) {
    return numb.toString(base);
    /* GeeksForGeeks article */
  }
  return baseConverter;
};
