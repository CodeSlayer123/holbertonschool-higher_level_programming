#!/usr/bin/node
const numbers = [];
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    numbers[i - 2] = process.argv[i];
  }
  numbers.sort().reverse();

  console.log(numbers[1]);
}
