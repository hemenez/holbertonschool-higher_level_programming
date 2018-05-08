#!/usr/bin/node
let request = require('request');
const filmUrl = process.argv[2];
const wedgeID = 'https://swapi.co/api/people/18/';
const options = {
  url: filmUrl,
  methods: 'GET'
};
request(options, function (err, res, body) {
  if (!err) {
    let json = JSON.parse(body);
    let { results } = json;
    let count = 0;
    for (let index = 0; index < results.length; index++) {
      let { characters } = results[index];
      for (let i = 0; i < characters.length; i++) {
        if (wedgeID === characters[i]) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
