#!/usr/bin/node
const newNumbers = [];
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2);
  for (const number of numbers) {
    if (isNaN(number) === false) {
      newNumbers.push(number);
    }
  }
  newNumbers.sort((a, b) => b - a);
  console.log(newNumbers[1]);
}
