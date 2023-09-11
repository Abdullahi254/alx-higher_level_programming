#!/usr/bin/node
import { argv } from 'node:process';

console.log(`My number: ${Number(argv[0]) === NaN ? "Not a number" : Number(argv[0])}`);