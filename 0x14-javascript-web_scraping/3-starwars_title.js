#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.io/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
