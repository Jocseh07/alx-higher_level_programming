#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    return;
  }
  const total = JSON.parse(body).results;
  const count = total.reduce((count, x) => {
    return count + x.characters.some((character) => character.endsWith('18/'));
  }, 0);
  console.log(count);
});
