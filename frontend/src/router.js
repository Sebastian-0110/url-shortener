import { createWebHistory, createRouter } from "vue-router";

import HomeView from "./components/HomeView.vue";
import UrlDetailsView from "./components/UrlDetailsView.vue";
import RedirectView from "@/components/RedirectView.vue";

const routes = [
	{ name: "home", path: "/", component: HomeView },
	{ name: "details", path: "/details/:urlCode", component: UrlDetailsView },
	{ name: "redirect", path: "/:urlCode", component: RedirectView },
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;