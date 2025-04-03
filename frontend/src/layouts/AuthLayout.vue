<script setup>
import { defineProps } from "vue";
import sitemap from "@/assets/sitemap";
import IconComponent from "@/components/IconComponent.vue";
import { submitForm } from "@/fx/api";

const props = defineProps({
  headline: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    default: "Login",
  },
  variant: {
    type: String,
    default: "user",
  },
  address: {
    type: String,
  },
});

const options = [
  {
    id: "register",
    type: "user",
    name: "Create an account",
    link: sitemap.auth.register,
  },
  {
    id: "login",
    type: "user",
    name: "Login",
    link: sitemap.auth.login,
  },
  {
    id: "forgot",
    type: "user",
    name: "Forgot Password ?",
    link: sitemap.auth.forgot,
  },
  {
    id: "register_professional",
    type: "professional",
    name: "Create an account",
    link: sitemap.auth.professional_register,
  },
  {
    id: "login_professional",
    type: "professional",
    name: "Login",
    link: sitemap.auth.professional_login,
  },
  {
    id: "forgot_professional",
    type: "professional",
    name: "Forgot Password ?",
    link: sitemap.auth.professional_forgot,
  },
];

const userTypes = [
  {
    id: "user",
    name: "User",
    link: sitemap.auth.login,
  },
  {
    id: "admin",
    name: "Admin",
    link: sitemap.auth.admin,
  },
  {
    id: "professional",
    name: "Professional",
    link: sitemap.auth.professional_login,
  },
];
</script>

<template>
  <div class="login-parent">
    <section class="image-parent">
      <img src="/img/interior.jpg" alt="" />
      <IconComponent />
    </section>
    <section class="form-parent">
      <h1>{{ props.headline }}</h1>
      <form method="post" @submit.prevent="(e) => submitForm(props.address, e)">
        <slot></slot>
      </form>
      <ul class="horizontal-list">
        <li
          v-for="option in options"
          :key="option.id"
          v-show="
            option.id !== props.type &&
            props.type !== 'admin' &&
            props.variant === option.type
          "
        >
          <a
            v-if="
              option.id !== props.type &&
              props.type !== 'admin' &&
              props.variant === option.type
            "
            :href="option.link"
            >{{ option.name }}</a
          >
        </li>
      </ul>
      <ul class="horizontal-list">
        <li v-for="option in userTypes" :key="option.id">
          <a v-if="option.id !== props.variant" :href="option.link">{{
            option.name
          }}</a>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.login-parent {
  height: 100%;
  display: flex;
}

section {
  width: 50%;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  position: relative;
}

.image-parent {
  overflow: hidden;
}

.form-parent {
  padding: var(--size-base);
  padding-top: var(--size-3xl);
  position: relative;
  gap: var(--size-sm);
  justify-content: center;
}

form {
  display: flex;
  flex-direction: column;
  position: relative;
  gap: var(--size-sm);
  justify-content: center;
}

.image-parent > img {
  object-fit: cover;
  position: absolute;
  top: -30%;
  left: -20%;
}

.logo {
  position: absolute;
  height: var(--font-xl);
  bottom: var(--size-base);
  left: var(--size-base);
  background-color: var(--accent-50);
  padding: 1px 8px 1px 10px;
  border-radius: var(--size-xs);
}

h1 {
  font-size: var(--font-xxl);
  text-align: center;
}

li,
a {
  color: var(--accent-600);
}

.variant {
  position: absolute;
  bottom: var(--size-base);
  right: var(--size-base);
}

.lst {
  list-style: none;
  display: flex;
  gap: var(--size-xs);
  margin: 0;
  padding: 0;
}
</style>
