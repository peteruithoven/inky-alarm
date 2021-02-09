<template>
  <div class="flex">
    <button
      v-for="(day, weekday) in days"
      :key="day"
      class="uppercase py-1 px-2 border-gray-200 border border-r-0 first:rounded-l-md last:rounded-r-md last:border-r"
      :class="{ 'bg-enabled text-gray-100': modelValue.includes(weekday) }"
      @click="toggle(weekday)"
    >
      {{ day }}
    </button>
  </div>
</template>

<script setup>
// modelValue contains list of enabled weekdays.
// weekday is an integer, where Monday is 0 and Sunday is 6
const props = defineProps({ modelValue: Array });
const emit = defineEmit(["update:modelValue"]);
const days = ["mo", "tu", "we", "th", "fr", "sa", "su"];

function toggle(weekday) {
  let { modelValue } = props;
  emit(
    "update:modelValue",
    modelValue.includes(weekday)
      ? modelValue.filter((i) => i !== weekday)
      : [...modelValue, weekday]
  );
}
</script>
