<template>
  <div class="w-min mx-auto py-5 space-y-5">
    <Card
      v-for="(alarm, index) of alarms"
      :key="index"
      class="space-y-5"
      :class="{ 'opacity-40': !alarm.enabled }"
    >
      <div class="flex justify-between items-center">
        <Toggle v-model="alarm.enabled" />
        <Time class="w-min" v-model="alarm.time" />
        <button @click="removeAlarm(index)">
          <ArchiveIcon class="h-8 w-8 text-gray-300" />
        </button>
      </div>
      <DaysSelection class="w-min" v-model="alarm.days" />
    </Card>
    <button
      class="bg-white shadow-md py-2 px-4 rounded-lg w-full text-lg hover:bg-enabled hover:text-gray-100 duration-100 ease-in-out min-w-max"
      @click="addAlarm()"
    >
      Add alarm
    </button>
  </div>
</template>

<script setup>
import { ref, watchEffect, watch, computed } from "vue";
import { ArchiveIcon } from "@vue-hero-icons/outline";
import throttle from "lodash/throttle";
import Card from "./components/Card.vue";
import Time from "./components/Time.vue";
import Toggle from "./components/Toggle.vue";
import DaysSelection from "./components/DaysSelection.vue";
import iconComptbl from "./utils/iconComptbl.js";
import { getAlarms, setAlarms } from "./api.js";

iconComptbl(ArchiveIcon);

let alarms = ref([]);

// alarms.value = await getAlarms();
getAlarms().then((newAlarms) => {
  alarms.value = newAlarms;
  watch(
    alarms.value,
    // TODO debug
    throttle((value) => {
      setAlarms(alarms.value);
    }),
    2000
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
</script>
