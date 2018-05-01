#!/usr/bin/node
let firstArg = parseInt(process.argv[2])
function factorial (firstArg) {
  if (firstArg <= 1 || isNaN(firstArg)) {
    return 1;
  }
  let finalRes = firstArg;
  while (firstArg-- > 2) {
    finalRes *= firstArg;
  }
  return finalRes;
}
let result = factorial(firstArg);
console.log(result);
