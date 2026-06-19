const { createServer } = require('./server');

const PORT = process.env.PORT || 3000;
const server = createServer();

server.listen(PORT, () => {
  console.log(`Transaction service listening on http://localhost:${PORT}`);
});
