#!/usr/bin/node
function add(a, b) {
    if (isNaN(a) && isNaN(b)) {
        console.log(a + b);
    } else {
        console.log(NaN);
    }
}

add(process.argv[2], process.argv[3]);