#!/usr/bin/node
let request = require('request');
let options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, function (err, res) {
  if (!err) {
    let { statusCode } = res;
    let codeResult = 'code: ' + statusCode;
    console.log(codeResult);
  }
});
