<script setup>
import { defineProps, defineEmits } from "vue";
const props = defineProps({
  options: {
    type: Array,
  },
  name: {
    type: String,
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
console.log(props.options);
</script>

<template>
  <div class="parent">
    <label v-if="label">{{ props.label }}</label>
    <select :name="props.name" :value="props.modelValue" @input="onInput">
      <option v-for="o in props.options" :key="o.id" :value="o.id">
        {{ o.name }}
      </option>
    </select>
    <div class="icon">
      <slot></slot>
      <!-- <component :is="props.icon" /> -->
    </div>
  </div>
</template>

<style scoped>
select,
select:focus,
select:active,
select:hover {
  border-radius: var(--size-sm);
  padding: 10px;
  padding-left: 40px;
  font-size: var(--font-base);
  border: 2px solid var(--accent-600);
  /* outline: none; */
  box-shadow: none;
  width: 100%;
}

.parent {
  display: flex;
  align-items: center;
  position: relative;
  gap: 5px;
  /* flex-direction: column; */
  align-items: start;
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
