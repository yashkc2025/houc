<script setup>
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import { fetchData } from "@/fx/api";
import ProfessionalLayout from "@/layouts/ProfessionalLayout.vue";
import { IconNumber } from "@tabler/icons-vue";
import { IconPassword } from "@tabler/icons-vue";
import { IconUser } from "@tabler/icons-vue";
import { IconAt } from "@tabler/icons-vue";
import { IconMapPinCode } from "@tabler/icons-vue";
import { IconHome } from "@tabler/icons-vue";
import { onMounted } from "vue";

const lst = [
  {
    name: "name",
    label: "Name",
    icon: IconUser,
    type: "text",
    max: 50,
  },
  {
    name: "email",
    label: "Email Address",
    icon: IconAt,
    type: "email",
    max: 50,
  },
  {
    name: "address",
    label: "Address",
    icon: IconHome,
    type: "text",
    max: 300,
  },
  {
    name: "experience",
    label: "Experience",
    icon: IconNumber,
    type: "text",
    max: 300,
  },
  {
    name: "pincode",
    label: "Pincode",
    icon: IconMapPinCode,
    type: "number",
    max: 6,
  },
];

onMounted(async () => {
  await fetchData();
});
</script>

<template>
  <ProfessionalLayout msg="Manage your account">
    <div class="account">
      <InputComponent
        v-for="l in lst"
        :key="l.label"
        :name="l.name"
        :label="l.label"
        :type="l.type"
        :max="l.max"
      >
        <component :is="l.icon"></component>
      </InputComponent>
      <ButtonComponent text="Update Profile"></ButtonComponent>
    </div>
    <div class="password">
      <h1>Update Password</h1>
      <InputComponent name="password" label="Old Password" type="password"
        ><IconPassword />
      </InputComponent>
      <InputComponent name="password" label="Old Password" type="password"
        ><IconPassword />
      </InputComponent>
      <ButtonComponent text="Update Password"></ButtonComponent>
    </div>
  </ProfessionalLayout>
</template>

<style scoped>
.account,
.password {
  display: flex;
  flex-direction: column;
  gap: var(--size-lg);
  margin-top: var(--size-lg);
}

h1 {
  /* margin: 0; */
  text-align: center;
  font-size: var(--font-xl);
}
</style>
