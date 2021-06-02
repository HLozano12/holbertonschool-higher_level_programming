#!/usr/bin/node
/*
print a message depending of the number of arguments passed
*/

const MyArgs = process.argv.slice(2);

if (MyArgs.length === 0){
    console.log('No argument');
}
    else if (MyArgs.length === 1){
    console.log('Argument found');
    }
    else {
    console.log('Arguments found');
    }
