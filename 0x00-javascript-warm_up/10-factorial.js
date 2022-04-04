#!/usr/bin/node

function factorialize (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n < 0) return;
  if (n < 2) return 1;
  return (n * factorialize(n - 1));
}
const n = parseInt(process.argv[2]);
console.log(factorialize(n));
