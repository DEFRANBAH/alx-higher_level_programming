#!/usr/bin/node
const [,, arg1, arg2] = process.argv;

function add(a, b) {
	return a + b;
}
console.log(add(parseInt(arg1) + parseInt(arg2)));
