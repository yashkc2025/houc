<script setup>
import { defineProps } from "vue";

const props = defineProps({
  type: {
    type: String,
    required: true,
  },
  text: {
    type: String,
    default: "Submit",
  },
  name: {
    type: String,
    default: "input box",
  },
});
</script>

<template>
  <button :type="props.type" :name="props.name">{{ props.text }}</button>
</template>

<style scoped>
button {
  border-radius: var(--size-sm);
  padding: 10px;
  font-size: var(--font-base);
  background: var(--accent-600);
  width: 100%;
  border: var(--accent-600);
  color: white;
  font-weight: bold;
  cursor: pointer;
}

button[type="submit"] {
  cursor: pointer;
}

button > a {
  color: white;
}
</style>
