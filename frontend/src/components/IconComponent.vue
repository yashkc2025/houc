<script setup>
import { IconRosetteFilled } from "@tabler/icons-vue";
import { defineProps } from "vue";

const props = defineProps({
  msg: {
    type: String,
    default: "/",
  },
});
</script>
<template>
  <a class="logo" :href="props.msg">
    <p>houc</p>
    <IconRosetteFilled size="30" fill="#198755" stroke="0" />
  </a>
</template>

<style scoped>
.logo {
  display: flex;
  align-items: center;
  gap: 5px;
}

p {
  font-family: "kotka";
  font-size: 25px;
  margin: 0;
  color: #198755;
}
</style>
