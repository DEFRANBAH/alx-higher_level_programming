#!/usr/bin/node
const [,, arg1, arg2] = process.argv;
if (arg1 !== undefined && arg2 !== undefined) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log('undefined');
}		
