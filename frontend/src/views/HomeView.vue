<script setup>
import AppLayout from "@/layouts/AppLayout.vue";
import {
  IconFlower,
  IconPaint,
  IconSoup,
  IconBath,
  IconHomeBolt,
  IconScissors,
  IconWashMachine,
} from "@tabler/icons-vue";
import sitemap from "@/assets/sitemap";
import { onMounted, ref } from "vue";
import { fetchData } from "@/fx/api";
import server from "@/assets/server";

const msgText = "What are you looking for ?";

const categories = {
  Salon: IconScissors,
  Electrician: IconHomeBolt,
  Plumbing: IconBath,
  Painting: IconPaint,
  Gardening: IconFlower,
  Cooking: IconSoup,
  Cleaning: IconWashMachine,
};
let options = ref([]);

onMounted(async () => {
  const data = await fetchData(server.service.get_types);
  options.value = data;
});
</script>

<template>
  <AppLayout :msg="msgText">
    <div class="app-body">
      <ul>
        <li v-for="i in options" :key="i.id">
          <a :href="sitemap.services.fn(i.name)">
            <component class="icon" :is="categories[i.name]"></component>
            <p>{{ i.name }}</p>
          </a>
        </li>
      </ul>
    </div>
  </AppLayout>
</template>

<style scoped>
.app-body {
  display: flex;
  flex-direction: column;
  gap: var(--size-base);
}
ul {
  list-style: none;
  display: flex;
  gap: var(--size-xs);
  padding: 0;
  flex-wrap: wrap;
  justify-content: center;
  /* overflow-x: scroll; */
}

li > a {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--accent-50);
  border-radius: var(--size-xs);
  padding: var(--size-sm);
  cursor: pointer;
}

.icon {
  --size: 60px;
  padding: var(--size-base) var(--size-lg);
  width: var(--size);
  height: var(--size);
}

p {
  margin: 0;
  font-weight: bold;
  color: var(--accent-600);
}
</style>
