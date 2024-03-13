#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arry = process.argv.slice(2).map(Number);
  const second = arry.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
