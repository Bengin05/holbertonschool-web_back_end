const { createServer } = require('node:http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const originalLog = console.log;
    const output = [];
    console.log = (message) => {
      output.push(message);
    };
    countStudents(database)
      .then(() => {
        console.log = originalLog;
        res.end(`This is the list of our students\n${output.join('\n')}`);
      })
      .catch((error) => {
        console.log = originalLog;
        res.end(`This is the list of our students\n${error.message}`);
      });
  }
});

app.listen(1245);
module.exports = app;
