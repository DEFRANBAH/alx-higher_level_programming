#!/usr/bin/node
const argsCount = process.argv.slice(2); // get arguments
if (argsCount.length === 0) {	// check if no arguments
  console.log('No argument');
}	else if (argsCount.length === 1) {	// check if 1 argument
	console.log('Argument found');
}	else {
	console.log('Arguments found');
}	// check if more than 1 argument

