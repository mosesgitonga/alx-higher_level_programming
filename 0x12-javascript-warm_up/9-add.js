#!/usr/bin/node

function add(a, b) {
  const args = process.argv;
  a = parseFloat(args[2])
  b = parseFloat(args[3])
  if (!isNaN(a) && !isNaN(b)) {
    let res = a + b
    console.log(res)
} else {
  console.log('NaN')
}
}
add()
