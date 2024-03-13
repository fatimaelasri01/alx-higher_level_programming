#!/usr/bin/node
const dict = require('./101-data.js').dict;
const occurences = {};

for (const key in dict) {
  const cpt = dict[key];
  if (cpt in occurences) {
    occurences[cpt].push(key);
  } else {
    occurences[cpt] = [key];
  }
}
console.log(occurences);
