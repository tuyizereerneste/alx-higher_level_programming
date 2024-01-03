#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const info = data.characters;
  for (const i of info) {
    request.get(i, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const itsData = JSON.parse(body1);
      console.log(itsData.name);
    });
  }
});
