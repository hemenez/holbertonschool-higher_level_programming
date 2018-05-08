#!/usr/bin/node
let request = require('request');
let myUrl = 'http://swapi.co/api/films/' + process.argv[2];
let options = {
  url: myUrl,
  method: 'GET'
};
request(options, function (err, res, body) {
  if (!err) {
    let json = JSON.parse(body);
    let { title } = json;
    console.log(title);
  }
});
