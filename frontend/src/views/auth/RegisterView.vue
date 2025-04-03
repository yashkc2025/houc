<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconMapPinCode, IconPhone } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";
import { IconHome } from "@tabler/icons-vue";
import { IconUser } from "@tabler/icons-vue";
import { IconAt } from "@tabler/icons-vue";
const introText =
  "Sign up and enjoy complete access to a variety of household services";

const inputList = [
  {
    type: "text",
    name: "email",
    placeholder: "Your email",
    icon: IconAt,
  },
  {
    type: "text",
    name: "name",
    placeholder: "Your name",
    icon: IconUser,
  },
  {
    type: "password",
    name: "password",
    placeholder: "Your password",
    icon: IconPassword,
  },
  {
    type: "text",
    name: "address",
    placeholder: "Your address",
    icon: IconHome,
  },
  {
    type: "text",
    name: "pincode",
    placeholder: "Your pincode",
    icon: IconMapPinCode,
    max: 6,
  },
  {
    type: "text",
    name: "phone",
    placeholder: "Phone Number",
    icon: IconPhone,
    max: 10,
  },
];
</script>

<template>
  <AuthLayout
    type="register"
    :headline="introText"
    variant="user"
    :address="server.auth.user_register"
  >
    <InputComponent
      v-for="i in inputList"
      :name="i.name"
      :placeholder="i.placeholder"
      :type="i.type"
      :key="i.name"
      :required="true"
      :max="i.max"
    >
      <component :is="i.icon"></component>
    </InputComponent>
    <ButtonComponent type="submit" text="Create an account" />
  </AuthLayout>
</template>
