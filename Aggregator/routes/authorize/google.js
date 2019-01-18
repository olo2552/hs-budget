const fsPromises = require('fs').promises;
const { google } = require('googleapis');
const { server } = require("../../server");

const CREDENTIALS_FILE = require("../../config/credentials");
const { client_id, client_secret, redirect_uris } = CREDENTIALS_FILE.web;

const oauth2Client = new google.auth.OAuth2(
  client_id,
  client_secret,
  redirect_uris[0],
);

const SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly'];

server.route({
  method: 'GET',
  path: '/auth/google/new/',
  handler: async (request, h) => {
    try {
      const {tokens} = await oauth2Client.getToken(request.query.code);
      console.log({tokens});

      await fsPromises.writeFile("./config/token.json", JSON.stringify(tokens));

      return tokens;
    } catch(err) {
      console.log(err);
    }
  },
});


server.route({
  method: ['POST', 'GET'],
  path: '/auth/google',
  handler(request, h) {
    const url = oauth2Client.generateAuthUrl({
      access_type: 'offline',
      scope: SCOPES,
      redirect_uri: redirect_uris[0],
    });

    console.log({url});

    return h.redirect(url);
  },
});
