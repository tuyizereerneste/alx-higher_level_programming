#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const fileContent = process.argv[3];
fs.writeFile(file, fileContent, function (error) {
  if (error) console.error(error);
});
