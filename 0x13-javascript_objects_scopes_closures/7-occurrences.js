#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let index = 0;
  let count = 0;
  while (index < list.length) {
    if (list[index] === searchElement) {
      count += 1;
    }
    index++;
  }
  return count;
};
