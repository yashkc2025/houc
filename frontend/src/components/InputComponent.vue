<script setup>
import { defineProps, defineEmits } from "vue";
// import { IconHome } from "@tabler/icons-vue";

const props = defineProps({
  type: {
    type: String,
    default: "text",
  },
  placeholder: {
    type: String,
    default: "Enter something",
  },
  name: {
    type: String,
    default: "text",
  },
  required: {
    type: Boolean,
    default: false,
  },
  height: {
    type: String,
  },
  width: {
    type: Number,
  },
  label: {
    type: String,
  },
  max: {
    type: Number,
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
    <input
      class="input-box"
      :type="props.type"
      :name="props.name"
      :placeholder="props.placeholder"
      :required="props.required"
      :style="{ height: props.height, width: props.width }"
      :maxlength="props.max"
      :value="props.modelValue"
      @input="onInput"
      @change="onInput"
    />
    <div class="icon">
      <slot></slot>
      <!-- <component :is="props.icon" /> -->
    </div>
  </div>
</template>

<style scoped>
input,
input:focus,
input:active,
input:hover {
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
