#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const data_to_write = process.argv[3];

fs.writeFile(filename, data_to_write, 'utf-8', (err) => {
    if (err) {
        console.log(err);
    }
    return;
});