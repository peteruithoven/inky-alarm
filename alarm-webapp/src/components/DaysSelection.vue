<template>
  <div class="flex">
    <button
      v-for="day of days"
      :key="day"
      class="uppercase py-1 px-2 border-gray-200 border border-r-0 first:rounded-l-md last:rounded-r-md last:border-r"
      :class="{ 'bg-enabled text-gray-100': modelValue.includes(day) }"
      @click="toggle(day)"
    >
      {{ day }}
    </button>
  </div>
</template>

<script setup>
const props = defineProps({ modelValue: Array });
const emit = defineEmit(["update:modelValue"]);
const days = ["mo", "tu", "we", "th", "fr", "sa", "su"];

function toggle(day) {
  let { modelValue } = props;
  emit(
    "update:modelValue",
    modelValue.includes(day)
      ? modelValue.filter((i) => i !== day)
      : [...modelValue, day]
  );
}
</script>
