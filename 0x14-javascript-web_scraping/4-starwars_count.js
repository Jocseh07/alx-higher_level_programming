#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    return;
  }
  const total = JSON.parse(body).results;
  const count = total.reduce((count, x) => {
    return count + x.characters.includes(
      'https://swapi-api.alx-tools.com/api/people/18/'
    );
  }, 0);
  console.log(count);
});
