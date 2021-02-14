async function req(url, options) {
  const response = await fetch(url, options);
  if (!response.ok) {
    throw Error(response.statusText);
  }
  return await response.json();
}

export function getAlarms() {
  return req("/api/alarms");
}

export function setAlarms(alarms) {
  return req("/api/alarms", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(alarms)
  });
}
