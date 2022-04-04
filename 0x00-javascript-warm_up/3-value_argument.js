#!/usr/bin/node
let myVar;
if (process.argv[2]) {
  myVar = process.argv[2];
} else {
  myVar = 'No argument';
}

console.log(myVar);
