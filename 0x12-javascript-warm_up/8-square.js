#!/usr/bin/node
let firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < firstArg; row++) {
    console.log('X'.repeat(firstArg));
  }
}
