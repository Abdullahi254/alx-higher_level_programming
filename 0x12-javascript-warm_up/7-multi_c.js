#!/usr/bin/node
import { argv } from 'node:process';

let x = Number(argv[0]);

while (x > 0) {
    console.log("C is fun");
    x -= 1;
}