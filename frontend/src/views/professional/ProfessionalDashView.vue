<script setup>
import server from "@/assets/server";
import { fetchData, postData } from "@/fx/api";
import { getDate } from "@/fx/utils";
import ProfessionalLayout from "@/layouts/ProfessionalLayout.vue";
import { IconCircleCheckFilled } from "@tabler/icons-vue";
import { IconSquareRoundedXFilled } from "@tabler/icons-vue";
import { onMounted, ref, watch } from "vue";

let open_request = ref([]);
let past_request = ref([]);

onMounted(async () => {
  const data = await fetchData(server.professionals.get_requests);
  past_request.value = data.filter(
    (item) => item.request_status === "complete"
  );
  open_request.value = data.filter(
    (item) => item.request_status !== "complete"
  );
});

const serviceLables = ["Name", "Phone", "Address", "Date", "Action"];
const pastLables = ["Name", "Phone", "Address", "Date", "Rating"];

watch(open_request, (o) => {
  console.log(o);
});
</script>

<template>
  <ProfessionalLayout>
    <div class="dash">
      <div>
        <div class="table-labels">
          <h3>New Requests</h3>
        </div>
        <table>
          <thead>
            <tr>
              <th v-for="l in serviceLables" :key="l">{{ l }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in open_request" :key="r.id">
              <td>{{ r.service.name }}</td>
              <td>{{ r.user.phone }}</td>
              <td>{{ r.user.address }}</td>
              <td>{{ getDate(r.date_created) }}</td>
              <td class="actions">
                <div>
                  <IconSquareRoundedXFilled
                    class="cancelled"
                    @click="
                      postData(server.professionals.reject_request, {
                        service_id: r.id,
                      })
                    "
                  />
                </div>
                <div>
                  <IconCircleCheckFilled
                    class="approved"
                    @click="
                      postData(server.professionals.accept_request, {
                        service_id: r.id,
                      })
                    "
                  />
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div>
        <div class="table-labels">
          <h3>Completed Requests</h3>
        </div>
        <table>
          <thead>
            <tr>
              <th v-for="l in pastLables" :key="l">{{ l }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in past_request" :key="r.id">
              <td>{{ r.service.name }}</td>
              <td>{{ r.user.phone }}</td>
              <td>{{ r.user.address }}</td>
              <td>{{ getDate(r.date_created) }}</td>
              <td>{{ r.review[0].rating }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </ProfessionalLayout>
</template>

<style scoped>
.actions {
  display: flex;
  gap: var(--size-sm);
}

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
td:nth-child(2) {
  width: 20%;
}

th:nth-child(3),
td:nth-child(3) {
  width: 30%; /* Adjust based on your needs */
}

th:last-child,
td:last-child {
  width: 5%; /* Gives more space to the Address column */
}
</style>
