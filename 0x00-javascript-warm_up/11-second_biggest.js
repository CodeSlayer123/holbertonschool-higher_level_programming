#!/usr/bin/node
const numbers = [];
for (let i = 2; i < process.argv.length; i++) {
  numbers[i - 2] = process.argv[i];
}
numbers.sort().reverse();
if (numbers[1] === undefined) {
  numbers[1] = 0;
}
console.log(numbers[1]);
