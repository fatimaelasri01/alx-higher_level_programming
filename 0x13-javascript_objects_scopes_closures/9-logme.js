#!/usr/bin/node
let nbrOfArgs = 0;
exports.logMe = function (item) {
  console.log(`${nbrOfArgs}: ${item}`);
  nbrOfArgs++;
};
