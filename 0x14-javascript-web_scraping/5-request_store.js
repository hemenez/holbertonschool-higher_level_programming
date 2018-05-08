#!/usr/bin/node
let fs = require('fs');
let request = require('request');
const myUrl = process.argv[2];
const filePath = process.argv[3];
const options = {
  url: myUrl,
  methods: 'GET',
  headers: {
    'content-type': 'text/plain; charset=utf-8'
  }
};
request(options, function (err, res, body) {
  if (!err) {
    fs.writeFile(filePath, body, 'utf8');
  }
});
