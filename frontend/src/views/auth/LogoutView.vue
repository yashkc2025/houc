<script setup>
import server from "@/assets/server";
import { fetchData } from "@/fx/api";
import router from "@/router";
import { onMounted } from "vue";

onMounted(async () => {
  await fetchData(server.auth.logout);

  router.push({ path: "/auth/login" });
});
</script>
