<script setup>
import server from "@/assets/server";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import SelectComponent from "@/components/SelectComponent.vue";
import TextAreaComponent from "@/components/TextAreaComponent.vue";
import { fetchData, submitForm } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconCategory, IconCoinRupee } from "@tabler/icons-vue";
import { IconAlignBoxTopLeft } from "@tabler/icons-vue";
import { IconClock } from "@tabler/icons-vue";
import { IconCarambola } from "@tabler/icons-vue";
import { onMounted, ref } from "vue";

const inputList = [
  {
    name: "name",
    label: "Name",
    type: "text",
    placeholder: "Service Name",
    icon: IconCarambola,
  },
  {
    name: "price",
    label: "Price",
    type: "number",
    placeholder: "Price",
    icon: IconCoinRupee,
  },
  {
    name: "time_required",
    label: "Time Required",
    type: "number",
    placeholder: "e.g. 2",
    icon: IconClock,
  },
];

let options = ref([]);

onMounted(async () => {
  const data = await fetchData(server.service.get_types);
  options.value = data;
});
</script>

<template>
  <AdminLayout msg="Create Service">
    <form @submit.prevent="(e) => submitForm(server.service.create_service, e)">
      <InputComponent
        v-for="i in inputList"
        :key="i"
        :name="i.name"
        :label="i.label"
        :type="i.type"
        :placeholder="i.placeholder"
      >
        <component :is="i.icon"></component>
      </InputComponent>
      <TextAreaComponent label="Description" name="description">
        <IconAlignBoxTopLeft />
      </TextAreaComponent>
      <SelectComponent
        :options="options"
        name="service_type"
        label="Service Category"
      >
        <IconCategory />
      </SelectComponent>
      <ButtonComponent>Create Service</ButtonComponent>
    </form>
  </AdminLayout>
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: var(--size-lg);
}
</style>
