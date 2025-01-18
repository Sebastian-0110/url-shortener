import { createWebHistory, createRouter } from "vue-router";

import HomeView from "./components/HomeView.vue";
import UrlDetailsView from "./components/UrlDetailsView.vue";

const routes = [
	{ path: "/", component: HomeView },
	{ path: "/details/:url_code", component: UrlDetailsView },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;