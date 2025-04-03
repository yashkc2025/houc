<script setup>
import { defineProps } from "vue";
import ProfessionalNavbarComponent from "@/components/ProfessionalNavbarComponent.vue";

const props = defineProps({
  msg: {
    type: String,
  },
});
</script>

<template>
  <div class="app-layout">
    <ProfessionalNavbarComponent />
    <section class="app-body-wrapper">
      <h1>{{ props.msg }}</h1>
      <slot></slot>
    </section>
  </div>
</template>

<style scoped>
.app-layout {
  display: flex;
  flex-direction: column;
}

.app-body-wrapper {
  padding: var(--size-sm) var(--size-md);
  margin-top: 50px;
}

h1,
.largest-text {
  /* margin: 0; */
  text-align: center;
  font-size: var(--font-xl);
}
</style>
