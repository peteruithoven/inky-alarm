<template>
  <input
    type="number"
    class="px-2 py-0.5 rounded-md spinner-none"
    v-model="value"
    @focus="$event.target.select()"
  />
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({ modelValue: Number, max: Number });
const emit = defineEmit(["update:modelValue"]);

const value = computed({
  get: () => props.modelValue.toString().padStart(2, "0"),
  set: (val) => {
    val = parseInt(val || "0");
    if (val > props.max) val = 0;
    if (val < 0) val = props.max;
    emit("update:modelValue", val);
  }
});
</script>
