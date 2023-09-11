#!/usr/bin/node

let x = Number(process.argv[2]);
let sum = "";

if (typeof (x) == "number") {
    for (let i = 0; i < x; i++) {
        sum = "";
        for (let j = 0; j < x; j++) {
            sum = sum + "X"
        }
        console.log(sum)
    }
} else {
    console.log("Missing size");
}