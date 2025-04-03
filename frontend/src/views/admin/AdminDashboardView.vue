<script setup>
import server from "@/assets/server";
import sitemap from "@/assets/sitemap";
import { fetchData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
// import { IconClockFilled } from "@tabler/icons-vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { onMounted, ref } from "vue";

let users = ref([]);
let professionals = ref([]);
let services = ref([]);
// let service_requests = ref([]);
onMounted(async () => {
  users.value = await fetchData(server.admin.get_users);
  professionals.value = await fetchData(server.professionals.get_professional);
  services.value = await fetchData(server.service.get_services);
  // service_requests.value = await fetchData(server.admin.get_requests);
});

const userLabels = ["Name", "Email", "Address"];
const professionalLables = ["Name", "Email", "Verified"];
const serviceLables = ["Name", "Price", "Category"];
// const requestLables = [
//   "Name",
//   "Price",
//   "Professional Email",
//   "User Email",
//   "Status",
// ];
</script>
<template>
  <AdminLayout msg="Welcome Admin">
    <div class="dash">
      <div>
        <div class="table-labels">
          <h3>Customers</h3>
          <a :href="sitemap.admin.manage_users" class="tablet">View More</a>
        </div>
        <table>
          <thead>
            <tr>
              <th v-for="l in userLabels" :key="l">{{ l }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in users" :key="r.id">
              <td>{{ r.name }}</td>
              <td>{{ r.email }}</td>
              <td>{{ r.address }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div>
        <div class="table-labels">
          <h3>Professionals</h3>
          <a :href="sitemap.admin.manage_professionals" class="tablet"
            >View More</a
          >
        </div>
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
              <td>
                <div class="status" href="">
                  <IconCircleCheckFilled
                    class="approved"
                    v-if="r.is_approved === true"
                  />
                  <IconSquareRoundedXFilled
                    class="cancelled"
                    v-if="r.is_approved === false"
                  />
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div>
        <div class="table-labels">
          <h3>Services</h3>
          <a :href="sitemap.admin.manage_services" class="tablet">View More</a>
        </div>
        <table>
          <thead>
            <tr>
              <th v-for="l in serviceLables" :key="l">{{ l }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in services" :key="r.id">
              <td>{{ r.name }}</td>
              <td>{{ r.price }}</td>
              <td>{{ r.service_type.name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- <div>
        <div class="table-labels">
          <h3>Service Requests</h3>
          <a :href="sitemap.admin.manage_requests" class="tablet">View More</a>
        </div>
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
      </div> -->
    </div>
  </AdminLayout>
</template>

<style scoped>
.dash {
  display: flex;
  flex-direction: column;
  gap: var(--size-xl);
}

th:first-child,
td:first-child {
  width: 30%; /* Adjust based on your needs */
}

th:nth-child(2),
td:nth-child(2),
th:nth-child(3),
td:nth-child(3) {
  width: 40%; /* Adjust based on your needs */
}

th:last-child,
td:last-child {
  width: 30%; /* Gives more space to the Address column */
}
</style>
