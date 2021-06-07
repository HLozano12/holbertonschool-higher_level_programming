#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments
all args CAN be Ints
If No arg passed, print "0"
If # of arg is one, print "0"
console.log to print output
*/

const theList = process.argv;
let l = 0;
let h = 0;
if (theList.length >= 4) {
  let numb;
  l = parseInt(theList[2]);
  for (let r = 3; r < theList.length; r++) {
    numb = parseInt(theList[r]);
    if (numb > l) {
      h = l;
      l = numb;
    } else if (numb < l && numb > h) {
      h = numb;
    }
  }
}
console.log(h);
