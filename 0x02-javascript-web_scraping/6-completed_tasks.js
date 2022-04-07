#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const done = {};
let count = 0;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const json = JSON.parse(body);

  for (let usrId = 1; usrId <= 10; usrId++) {
    count = 0;
    for (let i = 0; i < json.length; i++) {
      if (json[i].userId === usrId) {
        if (json[i].completed === true) {
          count++;
          done[usrId] = count;
        }
      }
    }
  }
  console.log(done);
});
