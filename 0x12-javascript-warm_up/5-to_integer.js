#!/usr/bin/node

console.log(`My number: ${Number(process.argv[2]) === NaN ? "Not a number" : Number(process.argv[2])}`);