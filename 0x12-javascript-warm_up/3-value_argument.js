#!/usr/bin/node
/*
print 1st arg passed to it
*/

const MyArgs = process.argv.slice(2);

if (typeof MyArgs[0] === 'undefined') {
  console.log('No argument');
} else {
  console.log(MyArgs[0]);
}
