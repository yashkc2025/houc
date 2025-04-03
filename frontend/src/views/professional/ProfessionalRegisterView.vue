<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import SelectComponent from "@/components/SelectComponent.vue";
import { fetchData } from "@/fx/api";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { IconCategory, IconNumbers, IconPhone } from "@tabler/icons-vue";
import { IconCertificate } from "@tabler/icons-vue";
import { IconBlockquote } from "@tabler/icons-vue";
import { IconMapPinCode } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";
import { IconHome } from "@tabler/icons-vue";
import { IconUser } from "@tabler/icons-vue";
import { IconAt } from "@tabler/icons-vue";
import { onMounted, ref } from "vue";
const introText = "Let's get started !";

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
    type: "file",
    name: "proof_document",
    placeholder: "Verification document",
    icon: IconCertificate,
  },
  {
    type: "txt",
    name: "description",
    placeholder: "Your description",
    icon: IconBlockquote,
  },
  {
    type: "number",
    name: "experience",
    placeholder: "Years of Experience",
    icon: IconNumbers,
  },
  {
    type: "number",
    name: "phone",
    placeholder: "Phone Number",
    icon: IconPhone,
    max: 10,
  },
];

let options = ref([]);

onMounted(async () => {
  const data = await fetchData(server.service.get_types);
  options.value = data;
});
</script>

<template>
  <AuthLayout
    type="register_professional"
    :headline="introText"
    variant="professional"
    :address="server.auth.professional_register"
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
    <SelectComponent :options="options" name="service_type">
      <IconCategory />
    </SelectComponent>
    <ButtonComponent text="Create an account" />
  </AuthLayout>
</template>
