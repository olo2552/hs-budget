const { google } = require('googleapis');
const CREDENTIALS_FILE = require("./credentials");
const TOKEN_FILE = require("./token");

const { client_id, client_secret, redirect_uris } = CREDENTIALS_FILE.web;
const { access_token } = TOKEN_FILE;

const oAuth2Client = new google.auth.OAuth2(
  client_id,
  client_secret,
  redirect_uris[0],
);

oAuth2Client.setCredentials({
  access_token,
});

module.exports = {
  googleClient: oAuth2Client
};