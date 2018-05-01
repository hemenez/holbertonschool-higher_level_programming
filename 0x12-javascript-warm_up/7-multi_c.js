#!/usr/bin/node
let checkVal = parseInt(process.argv[2]);
if (isNaN(checkVal)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < checkVal; index++) {
    console.log('C is fun');
  }
}
