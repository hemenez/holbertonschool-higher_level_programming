#!/usr/bin/node
let request = require('request');
let options = {
  url: process.argv[2],
  methods: 'GET'
};
request(options, function (err, res, body) {
  if (!err) {
    let json = JSON.parse(body);
    let tasksDict = {};
    for (let index = 0; index < json.length; index++) {
      let { userId } = json[index];
      let { completed } = json[index];
      if (completed === true) {
        if (userId in tasksDict) {
          tasksDict[userId] += 1;
        } else { tasksDict[userId] = 1; }
      }
    }
    console.log(tasksDict);
  }
});
