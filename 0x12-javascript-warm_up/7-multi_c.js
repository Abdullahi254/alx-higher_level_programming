#!/usr/bin/node


let x = Number(process.argv[2]);

if (typeof (x) == "number") {
    while (x > 0) {
        console.log("C is fun");
        x -= 1;
    }
} else {
    console.log("Missing number of occurrences");
}