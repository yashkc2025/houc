<script setup>
import server from "@/assets/server";
import { fetchData } from "@/fx/api";
import ProfessionalLayout from "@/layouts/ProfessionalLayout.vue";
import { onMounted, ref } from "vue";

const data = ref({});
let chartData = ref([]);

onMounted(async () => {
  data.value = await fetchData(server.professionals.professional_summary);
  chartData.value = Object.entries(data.value);
});
</script>

<template>
  <ProfessionalLayout msg="Summary">
    <div class="summary-parent">
      <div class="summary-top">
        <table>
          <thead>
            <tr>
              <th>Entity</th>
              <th>Count</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="i in Object.keys(data)" :key="i">
              <td>{{ i }}</td>
              <td>{{ data[i] }}</td>
            </tr>
          </tbody>
        </table>
        <div class="chart-wrapper">
          <column-chart
            :data="chartData"
            :colors="['#136942']"
            height="100%"
          ></column-chart>
        </div>
      </div>
      <!-- <div class="summary-bottom">
        <scatter-chart
          :data="chartData"
          :colors="['#136942']"
          xtitle="Size"
          ytitle="Rating"
        ></scatter-chart>
      </div> -->
    </div>
  </ProfessionalLayout>
</template>

<style scoped>
.summary-parent {
  display: flex;
  flex-direction: column;
  gap: var(--size-md);
}
.summary-top,
.summary-bottom {
  display: flex;
  flex-direction: row;
  height: 6%;
  gap: 20px;
}

.chart-wrapper {
  flex: 2;
}

table {
  flex: 1;
}
</style>
