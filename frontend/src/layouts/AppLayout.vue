<script setup>
import NavbarComponent from "@/components/NavbarComponent.vue";
import { defineProps } from "vue";

const props = defineProps({
  msg: {
    type: String,
  },
});
</script>

<template>
  <div class="app-layout">
    <NavbarComponent />
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
