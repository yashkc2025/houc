<script setup>
import AppLayout from "@/layouts/AppLayout.vue";
import { IconCarambolaFilled } from "@tabler/icons-vue";

const data = [
  {
    id: 1,
    professional: "Jason Gilbert",
    contact: 8918918912,
    rating: 3,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 3,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 3,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 4,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 5,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 5,
  },
  {
    id: 1,
    contact: 8918918912,
    professional: "Jason Gilbert",
    rating: 5,
  },
];
const labels = ["Professional Name", "Contact", "Rating"];
</script>

<template>
  <AppLayout msg="Choose a service professional">
    <table>
      <thead>
        <tr>
          <th v-for="l in labels" :key="l">{{ l }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in data" :key="r.id">
          <td>{{ r.professional }}</td>
          <td>{{ r.contact }}</td>
          <td class="rating">
            <span v-for="n in r.rating" :key="n">
              <IconCarambolaFilled class="icon star" />
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </AppLayout>
</template>

<style scoped>
.completed {
  filter: invert(16%) sepia(53%) saturate(6429%) hue-rotate(156deg)
    brightness(111%) contrast(80%);
}

.cancelled {
  filter: invert(12%) sepia(61%) saturate(6120%) hue-rotate(337deg)
    brightness(96%) contrast(94%);
}

.pending {
  filter: invert(72%) sepia(76%) saturate(2414%) hue-rotate(6deg)
    brightness(102%) contrast(94%);
}
</style>
