#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const total = JSON.parse(body).results;
  const char = total.filter((x) => {
    return x.characters.some((character) => character.endsWith('/18/'));
  });
  console.log(char.length);
});
