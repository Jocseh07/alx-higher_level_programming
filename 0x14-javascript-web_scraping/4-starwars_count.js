#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const total = JSON.parse(body).results;
  const char = total.filter((x) => {
    return x.characters.includes(
      'https://swapi-api.alx-tools.com/api/people/18/'
    );
  });
  console.log(char.length);
});
