#!/usr/bin/node
/*
print My number: <first argument converted in integer> if the first argument can be converted to an integer
*/

const MyArgs = process.argv.slice(2);

if (typeof MyArgs[0] === 'undefined' || isNaN(MyArgs[0])) {
  console.log('Not a number');
} else {
  console.log('My number: %i', MyArgs[0]);
}
