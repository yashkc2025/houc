import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./main.css";
import VueChartkick from "vue-chartkick";
import "chartkick/chart.js";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

const app = createApp(App);

app.use(router);
app.use(VueChartkick);
app.use(Toast);
app.mount("#app");
