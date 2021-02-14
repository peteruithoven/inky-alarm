<template>
  <div class="w-min mx-auto pt-5 space-y-5 relative min-h-screen">
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
    <transition-group
      tag="div"
      class="sticky bottom-0 space-y-3 mx-auto"
      :class="{ 'pb-3': messages.length > 0 }"
      leave-active-class="transition-opacity ease-out duration-200"
      leave-to-class="opacity-0"
      enter-from-class="opacity-0 translate-y-4"
      enter-active-class="transition ease-out duration-200 translate"
    >
      <Message
        v-for="message of messages"
        :key="message.id"
        v-bind="message"
        @close="hideMessage($event)"
      />
    </transition-group>
  </div>
</template>

<script setup>
import { ref, watchEffect, watch, computed } from "vue";
import { ArchiveIcon } from "@vue-hero-icons/outline";
import Card from "./components/Card.vue";
import Time from "./components/Time.vue";
import Toggle from "./components/Toggle.vue";
import DaysSelection from "./components/DaysSelection.vue";
import Message from "./components/Message.vue";
import iconComptbl from "./utils/iconComptbl.js";
import useMessages from "./composables/useMessages.js";
import useAlarms from "./composables/useAlarms.js";

iconComptbl(ArchiveIcon);

const { messages, showMessage, showError, hideMessage } = useMessages();
const { alarms, addAlarm, removeAlarm } = useAlarms(showError);
</script>
