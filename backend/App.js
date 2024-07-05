const { createServer } = require('node:http');
//const hostname = '127.0.0.1';
const express = require('express')
const app = express();
const port = 8000;



app.get('/', (req, res) => {
res.status(200).send("hello world");
})

// set up server
app.listen(port,  () => {
  console.log(`Server running at http://:${port}/`);
});