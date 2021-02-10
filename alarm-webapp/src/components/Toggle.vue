<template>
  <div
    class="w-16 h-10 bg-gray-300 rounded-full flex-shrink-0 p-1 duration-300 ease-in-out"
    :class="{ 'bg-enabled': modelValue }"
    @click="emit('update:modelValue', !modelValue)"
  >
    <div
      class="bg-white w-8 h-8 rounded-full shadow-md transform duration-300 ease-in-out"
      :class="{ 'translate-x-6': modelValue }"
    ></div>
  </div>
</template>

<script setup>
const props = defineProps({ modelValue: Boolean });
const emit = defineEmit(["update:modelValue"]);
</script>
