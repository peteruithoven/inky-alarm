const express = require("express");
const { readJSON, writeJSON } = require("@bevry/jsonfile");
const os = require("os");
const path = require("path");
const app = express();
const filePath = path.join(os.homedir(), "/alarms.json");
const port = 3000;

app.use(express.static("dist"));
app.use(express.json());
// app.use(express.bodyParser());

let alarms = [
  {
    time: {
      hours: 7,
      minutes: 0
    },
    enabled: true,
    days: ["mo", "tu", "we"]
  }
];

readJSON(filePath).then((contents) => {
  alarms = contents;
  console.log("alarms: ", alarms);
});

app.get("/api/alarms", (req, res) => {
  res.send(alarms);
});
app.post("/api/alarms", (req, res) => {
  // console.log(req.body); // your json
  alarms = req.body;
  writeJSON(filePath, alarms).then(() => console.log("done"));
  res.send(alarms);
});

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`);
});
