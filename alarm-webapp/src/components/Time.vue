<template>
  <div
    class="rounded-md bg-white border-gray-200 border flex text-3xl items-center"
  >
    <NumberInput class="w-12" v-model="modelValue.hours" :max="23" />
    :
    <NumberInput class="w-12" v-model="modelValue.minutes" :max="59" />
  </div>
</template>

<script setup="props">
import { defineProps } from "vue";
import NumberInput from "./NumberInput.vue";

defineProps({
  modelValue: {
    hours: Number,
    minutes: Number
  }
});
</script>
