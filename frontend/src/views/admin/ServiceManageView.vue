<script setup>
import server from "@/assets/server";
import sitemap from "@/assets/sitemap";
import InputComponent from "@/components/InputComponent.vue";
import { fetchData, postData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconSearch } from "@tabler/icons-vue";
import { IconPlus } from "@tabler/icons-vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

let services = ref([]);

let searchText = ref("");

async function fetchServices() {
  services.value = await fetchData(server.service.get_services, {
    search_text: searchText.value,
  });
}

onMounted(fetchServices);
watch(searchText, async () => {
  await fetchServices();
});

const serviceLabels = [
  "Id",
  "Name",
  "Price",
  "Service Type",
  "Time Required",
  "Delete",
];

async function deleteService(id) {
  await postData(server.admin.delete_service, {
    service_id: id,
  });
}
</script>

<template>
  <AdminLayout msg="Manage Services">
    <div class="table-labels">
      <a :href="sitemap.admin.create_service" class="tablet">
        <IconPlus />
      </a>
      <InputComponent v-model="searchText">
        <IconSearch />
      </InputComponent>
    </div>
    <table>
      <thead>
        <tr>
          <th v-for="l in serviceLabels" :key="l">{{ l }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in services" :key="r.id">
          <td>{{ r.id }}</td>
          <td>{{ r.name }}</td>
          <td>{{ r.price }}</td>
          <td>{{ r.service_type.name }}</td>
          <td>{{ r.time_required }}</td>
          <td>
            <div>
              <IconSquareRoundedXFilled
                @click="deleteService(r.id)"
                class="cancelled"
              />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </AdminLayout>
</template>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  gap: var(--size-sm);
}
th:first-child,
td:first-child {
  width: 10%; /* Adjust based on your needs */
}

th:nth-child(2),
td:nth-child(2),
th:nth-child(3),
td:nth-child(3) {
  width: 20%; /* Adjust based on your needs */
}

th:last-child,
td:last-child {
  width: 50%; /* Gives more space to the Address column */
}

.table-labels {
  margin-bottom: 10px;
  display: flex;
  flex-direction: row;
}
</style>
