#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const total = JSON.parse(body).results;
  console.log(total.reduce((acc, film) => {
    return acc + film.characters.length;
  }));
});
