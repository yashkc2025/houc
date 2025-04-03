<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconAt } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";

const introText = "One stop solution for all your needs";

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
    type="login"
    :headline="introText"
    variant="user"
    :address="server.auth.user_login"
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
