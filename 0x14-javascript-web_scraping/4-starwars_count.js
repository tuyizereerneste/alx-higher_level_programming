#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const filta = data.results.filter(film => {
      return film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
    });
    const number = filta.length;
    console.log(number);
  }
});
