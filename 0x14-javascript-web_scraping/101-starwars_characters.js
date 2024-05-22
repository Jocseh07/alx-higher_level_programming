#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const total = JSON.parse(body).characters;
  printName(total, 0);
});

function printName (actors, index) {
  request(actors[index], (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const actor = JSON.parse(body).name;
    console.log(actor);
    if (actors[index + 1]) {
      printName(actors, index + 1);
    }
  });
}
