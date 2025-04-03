<script setup>
import { IconSettings } from "@tabler/icons-vue";
import { IconDoorExit } from "@tabler/icons-vue";
import { IconHistory } from "@tabler/icons-vue";
import { IconUser } from "@tabler/icons-vue";
import { ref } from "vue";
import IconComponent from "@/components/IconComponent.vue";
import { IconSquareRoundedX } from "@tabler/icons-vue";
// import InputComponent from "./InputComponent.vue";
// import { IconSearch } from "@tabler/icons-vue";
import sitemap from "@/assets/sitemap";

const navItems = [
  {
    link: sitemap.account.config,
    label: "Account",
    icon: IconSettings,
  },
  {
    link: sitemap.services.history,
    label: "History",
    icon: IconHistory,
  },

  {
    link: sitemap.auth.logout,
    label: "Logout",
    icon: IconDoorExit,
  },
];

const showMenu = ref(false);
</script>

<template>
  <section class="navbar">
    <IconComponent />
    <!-- <InputComponent
      name="searchText"
      placeholder="Something specific ✨"
      :required="true"
      height="10px"
      width="50vw"
    >
      <IconSearch height="20px" />
    </InputComponent> -->
    <div class="flex-row">
      <ul class="horizontal-list">
        <li>
          <a :href="sitemap.services.search">Search </a>
        </li>
      </ul>
      <IconUser class="icon" @click="showMenu = !showMenu" v-if="!showMenu" />
      <IconSquareRoundedX
        class="icon"
        @click="showMenu = !showMenu"
        v-if="showMenu"
      />
      <ul
        class="horizontal-list hidden-menu"
        v-if="showMenu"
        @click="showMenu = !showMenu"
      >
        <li v-for="option in navItems" :key="option.label">
          <a :href="option.link"
            >{{ option.label }}

            <component class="icon navIcon" :is="option.icon"></component>
          </a>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.flex-row {
  display: flex;
  flex-direction: row;
  gap: var(--size-md);
  align-items: end;
}
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

.hidden-menu {
  display: flex;
  flex-direction: column;
  background-color: var(--accent-50);
  position: absolute;
  right: var(--size-sm);
  top: 45px;
  padding: var(--size-sm);
  border-radius: var(--size-xs);
  border: 2px solid var(--accent-500);
}

a {
  display: flex;
  flex-direction: row;
  gap: 20px;
  align-items: center;
  justify-content: space-between;
}

.navIcon:hover,
a:hover > svg {
  filter: none;
}

.navIcon {
  height: 20px;
}
</style>
