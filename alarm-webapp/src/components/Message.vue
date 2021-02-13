<template>
  <div class="rounded-md w-full flex justify-between" :class="color">
    <span class="pl-3 py-3">{{ text }}</span>
    <button class="p-3" @click="emit('close', id)">
      <XIcon />
    </button>
  </div>
</template>

<script setup>
import { computed, defineEmit } from "vue";
import { XIcon } from "@vue-hero-icons/outline";
import iconComptbl from "../utils/iconComptbl.js";
iconComptbl(XIcon);

const props = defineProps({ id: Number, type: String, text: String });
const emit = defineEmit(["close"]);

const color = computed(() => {
  switch (props.type) {
    case "error":
      return "bg-red-400";
    case "warning":
      return "bg-yellow-400";
    default:
      return "bg-blue-400";
  }
});
</script>
