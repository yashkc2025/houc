<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconAt } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";

const introText = "Ready for some work !";

const inputList = [
  {
    type: "text",
    name: "email",
    placeholder: "Your email",
    icon: IconAt,
  },
  {
    type: "password",
    name: "password",
    placeholder: "Your password",
    icon: IconPassword,
  },
];
</script>

<template>
  <AuthLayout
    type="login_professional"
    :headline="introText"
    variant="professional"
    :address="server.auth.professional_login"
  >
    <InputComponent
      v-for="i in inputList"
      :name="i.name"
      :placeholder="i.placeholder"
      :type="i.type"
      :key="i.name"
      :required="true"
    >
      <component :is="i.icon"></component>
    </InputComponent>
    <ButtonComponent text="Login" />
  </AuthLayout>
</template>
