#!/usr/bin/node
const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < x; a++) {
    console.log('X'.repeat(x));
  }
}
