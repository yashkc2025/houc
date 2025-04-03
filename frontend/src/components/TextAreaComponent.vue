<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  placeholder: {
    type: String,
    default: "Enter something",
  },
  name: {
    type: String,
    default: "text",
  },
  label: {
    type: String,
  },
  modelValue: {
    type: String,
  },
});

const emit = defineEmits(["update:modelValue"]);
const onInput = (event) => {
  emit("update:modelValue", event.target.value);
};
</script>

<template>
  <div class="parent">
    <label v-if="label">{{ props.label }}</label>
    <textarea
      :name="props.name"
      :placeholder="props.placeholder"
      :value="props.modelValue"
      @input="onInput"
      @change="onInput"
    ></textarea>
    <div class="icon">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
textarea {
  border-radius: var(--size-sm);
  padding: 10px;
  padding-left: 40px;
  font-size: var(--font-base);
  border: 2px solid var(--accent-600);
  /* outline: none; */
  box-shadow: none;
  width: 100%;
  margin: 0;
}

.parent {
  display: flex;
  align-items: center;
  position: relative;
  gap: 5px;
  /* flex-direction: column; */
  align-items: start;
  width: 100%;
}

.icon {
  position: absolute;
  left: 10px;
  top: 20%;
  /* height: 25px; */
}

label {
  font-weight: bold;
  font-size: var(--font-sm);
  /* padding-left: 5px; */
  /* left: 10px; */
  top: -20px;
  position: absolute;
}
</style>
