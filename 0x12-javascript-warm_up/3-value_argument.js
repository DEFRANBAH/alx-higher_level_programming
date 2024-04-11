#!/usr/bin/node
const [,, ...args] = process.argv;
if (args.length === 0) {
	console.log('No argument');	
} else (args.length === 1) 
{			
	console.log(args[0]);
}
