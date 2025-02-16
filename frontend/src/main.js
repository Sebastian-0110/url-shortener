import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router';

import { createNotivue } from "notivue";
import "notivue/notification.css";
import "notivue/animations.css";

const notivue = createNotivue({
	position: "top-center",
	limit: 10,
	enqueue: true,
	notifications: {
		global: {
			duration: 2000,
		}
	}
});

createApp(App)
	.use(router)
	.use(notivue)
	.mount('#app')
