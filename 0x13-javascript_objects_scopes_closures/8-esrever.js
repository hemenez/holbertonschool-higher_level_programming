#!/usr/bin/node
exports.esrever = function (list) {
  let index = list.length - 1;
  let revArr = [];
  while (index >= 0) {
    revArr.push(list[index]);
    index--;
  }
  return revArr;
};
