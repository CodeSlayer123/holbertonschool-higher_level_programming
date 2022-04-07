#!/usr/bin/node
const request = require('request');

const url2 = 'https://swapi-api.hbtn.io/api/people/18';
request(url2, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const json = JSON.parse(body);
  console.log(json.films.length);
});
