#!/usr/bin/node
/*
print "C is Fun" x amount of times
*/

const MyArgs = process.argv.slice(2);

const number = MyArgs[0];
let x;

if (typeof number === 'undefined' || isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < number; x++) {
    console.log('C is fun');
  }
}
