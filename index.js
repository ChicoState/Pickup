const express = require('express');
const path = require('path');
const app = express();
const port = 8080;

// Serve index.html for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Serve forum.html for the /forum URL
app.get('/forum', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'forum.html'));
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});