const Hapi = require('hapi');

const server = Hapi.server({
  port: process.env.SERVER_PORT,
  host: process.env.SERVER_HOST
});

module.exports = { server };