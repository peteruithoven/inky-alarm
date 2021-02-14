import { ref, watch } from "vue";
import throttle from "lodash/throttle";
import { getAlarms, setAlarms } from "../api.js";

export default function useAlarms(showError) {
  let alarms = ref([]);

  async function saveAlarms() {
    try {
      await setAlarms(alarms.value);
    } catch (error) {
      showError("Could not save alarms: " + error.message);
    }
  }

  getAlarms()
    .then((newAlarms) => {
      alarms.value = newAlarms;
      watch(alarms.value, throttle(saveAlarms, 1000));
    })
    .catch((error) => {
      showError("Could not get alarms: " + error.message);
    });

  function addAlarm() {
    alarms.value.push({
      time: {
        hours: 0,
        minutes: 0
      },
      enabled: true,
      days: []
    });
  }

  function removeAlarm(index) {
    alarms.value.splice(index, 1);
  }

  return {
    alarms,
    addAlarm,
    removeAlarm
  };
}
