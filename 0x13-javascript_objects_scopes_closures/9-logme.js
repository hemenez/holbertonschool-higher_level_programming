#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  let myStr = counter + ': ' + item;
  console.log(myStr);
  counter += 1;
};
