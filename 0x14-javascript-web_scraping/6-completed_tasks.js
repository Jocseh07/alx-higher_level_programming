#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const content = (JSON.parse(body));
  const total = {};
  for (const user of content) {
    if (user.completed === true) {
      if (user.userId in total) {
        total[user.userId] += 1;
      } else {
        total[user.userId] = 1;
      }
    }
  }
  console.log(total);
});
