#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const data = JSON.parse(body);
  data.characters.forEach((char) => {
    request.get(char, (error1, response1, body1) => {
      if (error1) {
        console.error('error:', error1);
      }
      const OneCharacter = JSON.parse(body1);
      console.log(OneCharacter.name);
    });
    return 0;
  });
});
