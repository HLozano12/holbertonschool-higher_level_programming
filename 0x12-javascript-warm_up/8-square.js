#!/usr/bin/node
/*
print a square
  Use x to print square
  use console.log
  if arg not covert to int, print "missing size"
*/

const MyArgs = process.argv.slice(2);

const number = MyArgs[0];
let x;

if (parseInt(number)) {
  for (x = 0; x < number; x++) {
    str += 'X';
  }
  
}
