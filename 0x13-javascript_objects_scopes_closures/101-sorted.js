#!/usr/bin/node
const dict = require('./101-data.js').dict;
const keys = Object.keys(dict);
const values = Object.values(dict);
const valuesSet = [...new Set(values)];
newDict = {};
for (const v of valuesSet) {
  const newList = [];
  for (let a = 0; a < values.length; a++) {
    if (values[a] === v) {
      newList.push(keys[a]);
    }
  }
  newDict[v] = newList;
}
console.log(newDict);
