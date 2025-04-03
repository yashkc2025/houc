<script setup>
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconAt } from "@tabler/icons-vue";
const introText = "Forgot your password ?";
</script>

<template>
  <AuthLayout type="forgot" :headline="introText" variant="user">
    <InputComponent type="text" name="user-email" :required="true">
      <IconAt />
    </InputComponent>
    <ButtonComponent text="Email a link" />
  </AuthLayout>
</template>
