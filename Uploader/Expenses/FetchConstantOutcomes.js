const _ = require("lodash");
const { google } = require("googleapis");
const { googleClient } = require("../config/googleClient");

const fetchConstantOutcomes = () => {
  const sheets = google.sheets({
    version: 'v4',
    auth: googleClient,
  });

  return sheets.spreadsheets.values.get({
    spreadsheetId: process.env.CONSTANT_OUTCOMES_SPREADSHEET_ID,
    range: 'Sheet1!A:B'
  })
    .then((res) => {
      console.log("response: ", res.data.values);
      return res.data.values;
    })
    .then(_.fromPairs)
    .catch((err) => {
      console.log('The GoogleAPI have thrown an error during spreadsheet fetching: ' + err);
    })
};

module.exports = { fetchConstantOutcomes };
