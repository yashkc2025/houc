<script setup>
import server from "@/assets/server";
import { fetchData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { IconClockFilled } from "@tabler/icons-vue";
// import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { onMounted, ref } from "vue";

let service_requests = ref([]);

async function fetchUsers() {
  service_requests.value = await fetchData(server.admin.get_requests, {});
}

onMounted(fetchUsers);

const requestLables = [
  "Name",
  "Price",
  "Professional Email",
  "User Email",
  "Status",
];

// async function blockProfessional(id) {
//   await postData(server.admin.block_user, {
//     user_id: id,
//   });
// }

// async function unBlockProfessional(id) {
//   await postData(server.admin.unblock_user, {
//     user_id: id,
//   });
// }
</script>

<template>
  <AdminLayout msg="Manage Users">
    <div class="app-wrapper">
      <table>
        <thead>
          <tr>
            <th v-for="l in requestLables" :key="l">{{ l }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in service_requests" :key="r.id">
            <td>{{ r.name }}</td>
            <td>{{ r.price }}</td>
            <td>{{ r.professional_email }}</td>
            <td>{{ r.user_email }}</td>
            <td>
              <div class="status" href="">
                <IconCircleCheckFilled
                  class="approved"
                  v-if="r.status === 'completed'"
                />
                <IconClockFilled
                  class="pending"
                  v-if="r.is_approved != 'completed'"
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
