<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import { fetchData, submitForm } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconAt, IconPassword } from "@tabler/icons-vue";
import { onMounted, ref } from "vue";

const lst = [
  {
    name: "email",
    label: "Email Address",
    icon: IconAt,
    type: "email",
    max: 50,
  },
];

const userData = ref({
  email: "",
});

onMounted(async () => {
  const data = await fetchData(server.account.user_details);
  userData.value = {
    email: data.email,
  };
});
</script>

<template>
  <AdminLayout msg="Manage your account">
    <form
      method="post"
      @submit.prevent="(e) => submitForm(server.account.update_user_details, e)"
      class="account"
    >
      <InputComponent
        v-for="l in lst"
        :key="l.label"
        :name="l.name"
        :label="l.label"
        :type="l.type"
        :max="l.max"
        v-model="userData[l.name]"
      >
        <component :is="l.icon"></component>
      </InputComponent>
      <ButtonComponent text="Update Profile"></ButtonComponent>
    </form>
    <form class="password">
      <h1>Update Password</h1>
      <InputComponent name="old_password" label="Old Password" type="password"
        ><IconPassword />
      </InputComponent>
      <InputComponent name="new_password" label="New Password" type="password"
        ><IconPassword />
      </InputComponent>
      <ButtonComponent text="Update Password"></ButtonComponent>
    </form>
  </AdminLayout>
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
