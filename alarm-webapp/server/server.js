#!/usr/bin/env node
import express from "express";
import { readJSON, writeJSON } from "@bevry/jsonfile";
import os from "os";
import path from "path";
const app = express();
const filePath = path.join(os.homedir(), "/alarms.json");
const port = 3000;

console.log("filePath: ", filePath);

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
    days: [0, 1, 2]
  }
];

try {
  alarms = await readJSON(filePath);
} catch (e) {
  console.log("error reading alarms: ", e);
  console.log("create new alarms file");
  await writeJSON(filePath, alarms);
}
console.log("alarms: ", alarms);

app.get("/api/alarms", (_, res) => {
  res.send(alarms);
});
app.post("/api/alarms", (req, res) => {
  // console.log(req.body); // your json
  alarms = req.body;
  writeJSON(filePath, alarms).then(() => console.log("updated alarms"));
  res.send(alarms);
});

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`);
});
