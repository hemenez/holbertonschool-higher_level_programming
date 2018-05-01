#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let arrayVals = process.argv.splice(2);
  let myArray = Array.from(arrayVals);
  let highestVal = Math.max(...myArray);
  let secondArr = [];
  for (let index = 0; index < arrayVals.length; index++) {
    if (arrayVals[index] < highestVal) {
      secondArr.push(arrayVals[index]);
    }
  }
  let secondHigh = Math.max(...secondArr);
  console.log(secondHigh);
}
