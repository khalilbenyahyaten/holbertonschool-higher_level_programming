#!/usr/bin/node
let x = 0;
process.argv.forEach((val, index) => {
  x++;
});
if (x < 3) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
