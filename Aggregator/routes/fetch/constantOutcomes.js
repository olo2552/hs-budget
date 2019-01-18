const { server } = require("../../server");
const { fetchConstantOutcomes } = require("../../Expenses/FetchConstantOutcomes");

server.route({
  method: 'GET',
  path: '/outcomes/constant',
  handler: async (request, h) => {
    return fetchConstantOutcomes();
  },
});
