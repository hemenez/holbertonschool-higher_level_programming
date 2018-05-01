#!/usr/bin/node
let checkVal = parseInt(process.argv[2]);
if (isNaN(checkVal)) {
  console.log('Not a number');
} else {
  console.log(checkVal);
}
