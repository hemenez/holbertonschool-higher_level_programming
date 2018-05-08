#!/usr/bin/node
let request = require('request');
let options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function(err, res) {
  let { statusCode } = res;
  codeResult = 'code: ' + statusCode;
  console.log(codeResult);
});
