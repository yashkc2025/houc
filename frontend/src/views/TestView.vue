<script setup>
import AppLayout from "@/layouts/AppLayout.vue";
import { useToast } from "vue-toastification";

const toast = useToast();

function notify() {
  toast.info("IIIIIIIIIII");
}
</script>

<template>
  <AppLayout>
    <button @click="notify">click me!</button>
  </AppLayout>
</template>
