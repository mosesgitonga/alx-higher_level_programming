#!/usr/bin/node
const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
const res = {};
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    const todo = data[i];
    if (todo.completed === true) {
      if (!res[todo.userId]) {
        res[todo.userId] = 1;
      } else {
        res[todo.userId] += 1;
      }
    }
  }
  console.log(res);
});
