#!/usr/bin/node
let myVar;
if (process.argv[3]) {
  myVar = 'Arguments found';
} else if (process.argv[2]) {
  myVar = 'Argument found';
} else {
  myVar = 'No argument';
}

console.log(myVar);
