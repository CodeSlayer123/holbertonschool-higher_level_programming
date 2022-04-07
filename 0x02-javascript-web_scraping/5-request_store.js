#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // json = JSON.parse(body)
  fs.writeFile(file, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
