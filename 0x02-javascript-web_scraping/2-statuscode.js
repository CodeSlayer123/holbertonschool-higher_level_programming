#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code: ' + response.statusCode);
});
