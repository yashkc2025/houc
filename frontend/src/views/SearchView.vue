<script setup>
import server from "@/assets/server";
import InputComponent from "@/components/InputComponent.vue";
import { fetchData, postData } from "@/fx/api";
import AppLayout from "@/layouts/AppLayout.vue";
import { IconSearch } from "@tabler/icons-vue";
import { IconPlus } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

let services = ref([]);
let professionals = ref([]);
let searchText = ref("");

onMounted(async () => {
  const data_services = await fetchData(server.service.get_services, {});
  const data_professionals = await fetchData(
    server.professionals.get_professional
  );
  services.value = data_services;
  professionals.value = data_professionals;
});

watch(searchText, async () => {
  const data_services = await fetchData(server.service.get_services, {
    search_text: searchText.value,
  });

  services.value = data_services;
});

const labels = ["Service", "Price", "Time Required", "Book"];
const professionalLables = ["Name", "Email", "Experience", "Book"];

let service_id = ref("");

function selectService(id) {
  const modal = document.getElementById("modal");
  modal.style.display = "block";
  service_id.value = id;
}

async function bookService(p_id) {
  postData(server.service.book_service, {
    professional_id: p_id,
    service_id: service_id.value,
  });
}

console.log(service_id);
</script>

<template>
  <AppLayout>
    <div class="app-wrapper">
      <InputComponent v-model="searchText">
        <IconSearch />
      </InputComponent>
      <table>
        <thead>
          <tr>
            <th v-for="l in labels" :key="l">{{ l }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in services" :key="r.id">
            <td>{{ r.name }}</td>
            <td>{{ "₹" + r.price }}</td>
            <td>{{ r.time_required + " hours" }}</td>
            <!-- <td class="rating">
            <span v-for="n in r.ratings" :key="n">
              <IconCarambolaFilled class="icon star" />
            </span>
          </td> -->
            <td>
              <IconPlus class="icon" @click="selectService(r.id)" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal" id="modal">
      <table>
        <thead>
          <tr>
            <th v-for="l in professionalLables" :key="l">{{ l }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in professionals" :key="r.id">
            <td>{{ r.name }}</td>
            <td>{{ r.email }}</td>
            <td>{{ r.experience + " Years" }}</td>
            <!-- <td class="rating">
            <span v-for="n in r.ratings" :key="n">
              <IconCarambolaFilled class="icon star" />
            </span>
          </td> -->
            <td>
              <IconPlus class="icon" @click="bookService(r.id)" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </AppLayout>
</template>

<style scoped>
.app-wrapper {
  display: flex;
  flex-direction: column;
  gap: var(--size-sm);
}
h1 {
  text-align: center;
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80vw;
  height: 80vh;
  background-color: var(--accent-100);
  border-radius: var(--size-sm);

  display: none;
}

.rating {
  text-wrap: nowrap;
}

.star {
  height: 20px;
}

th:first-child,
td:first-child {
  width: 30%;
}

th:nth-child(2),
td:nth-child(2) {
  width: 10%;
}

th:nth-child(3),
td:nth-child(3) {
  width: 10%; /* Adjust based on your needs */
}

th:last-child,
td:last-child {
  width: 5%; /* Gives more space to the Address column */
}
</style>
