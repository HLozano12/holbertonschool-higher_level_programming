#!/usr/bin/node
/*
script that prints the addition of 2 integers
1st arg is 1st int
2nd arg is 2nd int
Use prototype function add(a, b)
*/

function add (a, b) {
/* prototype */
  const aa = parseInt(a);
  const bb = parseInt(b);
  return aa + bb;
}
const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
