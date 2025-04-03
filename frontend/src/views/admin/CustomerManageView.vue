<script setup>
import server from "@/assets/server";
import InputComponent from "@/components/InputComponent.vue";
import { fetchData, postData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { IconSearch } from "@tabler/icons-vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

let users = ref([]);
let searchText = ref("");

async function fetchUsers() {
  users.value = await fetchData(server.admin.get_users, {
    search_text: searchText.value,
  });
}

onMounted(fetchUsers);

watch(searchText, async () => {
  await fetchUsers();
});
const userLabels = ["Id", "Name", "Email", "Address", "Status"];

async function blockProfessional(id) {
  await postData(server.admin.block_user, {
    user_id: id,
  });
}

async function unBlockProfessional(id) {
  await postData(server.admin.unblock_user, {
    user_id: id,
  });
}
</script>

<template>
  <AdminLayout msg="Manage Users">
    <div class="app-wrapper">
      <InputComponent v-model="searchText">
        <IconSearch />
      </InputComponent>
      <table>
        <thead>
          <tr>
            <th v-for="l in userLabels" :key="l">{{ l }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in users" :key="r.id">
            <td>{{ r.id }}</td>
            <td>{{ r.name }}</td>
            <td>{{ r.email }}</td>
            <td>{{ r.address }}</td>
            <td>
              <div class="status" href="">
                <IconCircleCheckFilled
                  class="approved"
                  v-if="r.is_blocked === false"
                  @click="blockProfessional(r.id)"
                />
                <IconSquareRoundedXFilled
                  class="cancelled"
                  v-if="r.is_blocked === true"
                  @click="unBlockProfessional(r.id)"
                />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </AdminLayout>
</template>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  gap: var(--size-sm);
}
table {
  width: 100%;
  border-collapse: collapse;
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
</style>
