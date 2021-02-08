export async function getAlarms() {
  const response = await fetch("/api/alarms");
  const json = await response.json();
  return json;
}
export async function setAlarms(alarms) {
  const response = await fetch("/api/alarms", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(alarms)
  });
  const json = await response.json();
  return json;
}
