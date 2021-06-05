#!/usr/bin/node

function add (x, y) {
    console.log(parseInt(x) + parseInt(x));
  }
  add(process.argv[2], process.argv[3]);
  