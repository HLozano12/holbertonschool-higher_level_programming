#!/usr/bin/node
/*
print two arguments to pass
*/

const MyArgs = process.argv.slice(2);

console.log('%s is %s', MyArgs[0], MyArgs[1]);
