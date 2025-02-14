import { createWebHistory, createRouter } from "vue-router";

import HomeView from "./components/HomeView.vue";
import UrlDetailsView from "./components/UrlDetailsView.vue";

const routes = [
	{ name: "home", path: "/", component: HomeView },
	{ name: "details", path: "/details/:uuid", component: UrlDetailsView },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;