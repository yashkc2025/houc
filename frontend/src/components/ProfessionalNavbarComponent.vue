<script setup>
import IconComponent from "@/components/IconComponent.vue";
import sitemap from "@/assets/sitemap";

const navItems = [
  // {
  //   link: sitemap.professional.search,
  //   label: "Search",
  // },
  {
    link: sitemap.account.professional_config,
    label: "Account",
  },
  {
    link: sitemap.professional.summary,
    label: "Summary",
  },
  {
    link: sitemap.auth.logout,
    label: "Logout",
  },
];
</script>

<template>
  <section class="navbar">
    <IconComponent msg="/professional" />
    <ul class="horizontal-list hidden-menu">
      <li v-for="option in navItems" :key="option.label">
        <a :href="option.link">{{ option.label }} </a>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  width: 95vw;
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  padding: var(--size-xs) var(--size-md);
  justify-content: space-between;
}

a {
  font-weight: 500;
}

ul {
  display: flex;
  flex-direction: row;
  gap: var(--size-lg);
}
</style>
