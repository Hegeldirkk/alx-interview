#!/usr/bin/node
/*
 * Write a script that prints all characters of a Star Wars movie
 * */
const request = require('request');
const idMov = process.argv.slice(2);
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + idMov;

function requestMov (array, index) {
  if (index === array.length) {
    return;
  }

  request(array[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      requestMov(array, index + 1);
    }
  });
}

request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chrList = JSON.parse(body).characters;
    requestMov(chrList, 0);
  }
});
