<script setup>
import server from "@/assets/server";
import InputComponent from "@/components/InputComponent.vue";
import { downloadFile, fetchData, postData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { IconSearch } from "@tabler/icons-vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

let users = ref([]);
let searchText = ref("");
let prof_id = ref();

async function fetchUsers() {
  users.value = await fetchData(server.professionals.get_professional, {
    search_text: searchText.value,
  });
}

onMounted(fetchUsers);

watch(searchText, async () => {
  await fetchUsers();
});

const userLabels = [
  "Id",
  "Name",
  "Email",
  "Address",
  "Status",
  "Services",
  "Approved",
];

async function blockProfessional(id) {
  await postData(server.admin.block_professional, {
    professional_id: id,
  });
}

async function unBlockProfessional(id) {
  await postData(server.admin.unblock_professional, {
    professional_id: id,
  });
}

function selectProf(id) {
  const modal = document.getElementById("modal");
  modal.style.display = "flex";
  prof_id.value = id;
}

async function approveProfessional() {
  await postData(server.admin.approve_professional, { prof_id: prof_id.value });
}

async function getDoc() {
  await downloadFile(`${server.admin.get_doc}?prof_id=${prof_id.value}`);
}
</script>

<template>
  <AdminLayout msg="Manage Professionals">
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
            <td>{{ r.service_type.name }}</td>
            <td>
              <div class="status" href="">
                <IconCircleCheckFilled
                  class="approved"
                  v-if="r.is_approved === true"
                />
                <IconSquareRoundedXFilled
                  class="cancelled"
                  v-if="r.is_approved === false"
                  @click="selectProf(r.id)"
                />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal" id="modal">
      <h1>Approve Professional</h1>
      <button class="styled-button" @click="getDoc()">View document</button>
      <button class="styled-button" @click="approveProfessional()">
        Approve
      </button>
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

h1 {
  text-align: center;
}
.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30vw;
  /* height: 60vh; */
  background-color: var(--accent-100);
  border-radius: var(--size-sm);
  display: none;
  flex-direction: column;
  gap: var(--size-sm);
  padding: var(--size-md);
}
</style>
