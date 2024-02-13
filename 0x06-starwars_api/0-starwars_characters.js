#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api';
const movieId = process.argv[2];
const apiUrl = `${endpoint}/films/${movieId}/`;

request(apiUrl, async function (error, response, body) {
  if(error) return console.log(error);

  let movieData = JSON.parse(body);
  let characters = movieData.characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(movieData.name);
          resolve(body);
        }
      });
    });
  }
});
