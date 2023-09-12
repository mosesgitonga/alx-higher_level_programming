#!/usr/bin/node

exports.esrever = function (list) {
  const listLen = list.length;
  const output = [];
  for (let i = listLen - 1; i >= 0; i--) {
    output.push(list[i]);
  }
  return output;
};
