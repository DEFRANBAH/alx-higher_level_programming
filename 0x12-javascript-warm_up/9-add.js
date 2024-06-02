#!/usr/bin/node

function add(a, b) {
	return a + b;
}
console.log(add(Number(process.argv[2]), Number(process.argv[3]))); // (p:arseInt(arg1) + parseInt(arg2)));
