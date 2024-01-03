#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const episodeId = process.argv[2];
request(apiUrl + episodeId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response) {
    const data = JSON.parse(body);
    const dataTitle = data.title;
    console.log(dataTitle);
  }
});
