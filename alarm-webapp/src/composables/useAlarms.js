import { ref, watch } from "vue";
import throttle from "lodash/throttle";
import { getAlarms, setAlarms } from "../api.js";

export default function useMessages() {
  let alarms = ref([]);

  getAlarms().then((newAlarms) => {
    alarms.value = newAlarms;
    watch(
      alarms.value,
      throttle((value) => {
        setAlarms(alarms.value);
      }, 1000)
    );
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
