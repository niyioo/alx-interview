#!/usr/bin/node
const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api';
const movieId = process.argv[2];
const apiUrl = `${endpoint}/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  for (const characterUrl of characters) {
    try {
      const characterData = await fetchCharacterData(characterUrl);
      console.log(characterData.name);
    } catch (error) {
      console.error('Error fetching character data:', error);
    }
  }
});

function fetchCharacterData(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}