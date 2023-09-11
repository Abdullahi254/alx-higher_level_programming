#!/usr/bin/node
import { argv } from 'node:process';

let x = Number(argv[0]);

if (typeof (x) == "number") {
    while (x > 0) {
        console.log("C is fun");
        x -= 1;
    }
} else {
    console.log("Missing number of occurrences");
}