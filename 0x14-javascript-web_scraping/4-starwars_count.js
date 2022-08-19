#!/usr/bin/node

const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    let numero = 0;
    for (const list of response.data.results) {
      for (const element of list.characters) {
        if (element.endsWith('18/')) {
          numero++;
          break;
        }
      }
    }
    console.log(numero);
  })
  .catch(function (error) {
    // handle error
    console.log('code :' + error.response.status);
  });
