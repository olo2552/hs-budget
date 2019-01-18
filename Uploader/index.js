require("dotenv").load({path: './config/.env'});

const { server } = require('./server');

require('./routes/authorize/google');
require("./routes/fetch/constantOutcomes");

const init = async () => {
  await server.start();

  console.log("Server running at:", server.info.uri);
};

process.on('unhandledRejection', (err) => {
  console.log(err);
  process.exit(1);
});

init();