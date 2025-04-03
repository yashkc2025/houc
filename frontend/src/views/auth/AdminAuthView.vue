<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconAt } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";

const introText = "Welcome home, Admin !";

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
    type="admin"
    :headline="introText"
    variant="admin"
    :address="server.auth.admin_login"
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
    <ButtonComponent text="Take me to the dashboard !" />
  </AuthLayout>
</template>
