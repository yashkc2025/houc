<script setup>
import server from "@/assets/server";
import { fetchData } from "@/fx/api";
import AdminLayout from "@/layouts/AdminLayout.vue";
import { onMounted, ref } from "vue";

let data = ref({});
let chartData = ref([]);
onMounted(async () => {
  data.value = await fetchData(server.admin.summary);
  chartData.value = Object.entries(data.value);
});
</script>

<template>
  <AdminLayout>
    <div class="summary-parent">
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
  </AdminLayout>
</template>

<style scoped>
.summary-parent {
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
