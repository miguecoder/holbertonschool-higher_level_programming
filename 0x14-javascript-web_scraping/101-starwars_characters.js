#!/usr/bin/node

const arg = process.argv[2];
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/' + arg)
  .then(async (response) => {
    for (const key of response.data.characters) {
      const sendRequest = async () => {
        try {
          const res = await axios.get(key);
          console.log(res.data.name);
        } catch (error) {
          console.error(error);
        }
      };
      await sendRequest();
    }
  });
