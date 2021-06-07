#!/usr/bin/node
/*
script that computes and prints a factorial
1st arg is Int
Fact of Nan = 1
Must use Func
must print with console.log()
*/

const theArgs = process.argv.slice(2);

if (typeof theArgs[0] === 'undefined' || isNaN(theArgs[0])) {
  console.log('%i', 1);
} else {
  console.log(factorial(theArgs[0]));
}

function factorial (h) {
  return (h !== 1) ? h * factorial(h - 1) : 1;
}
