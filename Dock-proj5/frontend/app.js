const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

app.get('/', async (req, res) => {
  try {
    const response = await axios.get('http://backend:5000/metrics');
    const lines = response.data.split('\n');
    const cpu = lines[0].split(' ')[1];
    const memory = lines[1].split(' ')[1];

    res.send(`
      <h1>Mini Monitor Dashboard</h1>
      <p><strong>CPU Usage:</strong> ${cpu}%</p>
      <p><strong>Memory Usage:</strong> ${memory} MB</p>
    `);
  } catch (err) {
    res.status(500).send("Error fetching metrics from backend.");
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on http://localhost:${PORT}`);
});

