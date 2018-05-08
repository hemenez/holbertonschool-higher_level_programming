#!/usr/bin/node
let request = require('request');
myUrl = 'http://swapi.co/api/films/' + process.argv[2];
let options = {
  url: myUrl,
  method: 'GET'
}
request(options, function(err, res, body) {
  let json = JSON.parse(body);
  let { title } = json;
  console.log(title);
});
