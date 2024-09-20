<script setup>
    import ShortenedUrlDisplay from "./components/ShortenedUrlDisplay.vue";
	import ShortenUrlForm from "./components/ShortenUrlForm.vue";
    import ErrorMessages from "./components/ErrorMessages.vue"

	import { reactive, ref } from "vue";

	const shortenedUrl = ref("");

    // This is a way of programatically changing the views without changing the url
	const displayState = reactive({
		state: {
			form: true,
			shortenedUrl: false,
			errorMessage: false,
		},

		show(view) {
			Object.keys(this.state).forEach((key) => {
				this.state[key] = false;
			});

			this.state[view] = true;
		},

		get_active(view) {
			return this.state[view];
		}
	});
</script>


<template>
    <div class="wrapper">
        <header class="header">
            <h1>Url shortener</h1>
        </header>

        <main class="main">
            <ShortenUrlForm 
                v-if="displayState.get_active('form')"
                v-model="shortenedUrl"
                :display-state
            />
            
            <ShortenedUrlDisplay 
                v-else-if="displayState.get_active('shortenedUrl')"		
                :shortened-url
                :display-state
            />

            <ErrorMessages v-else :display-state="displayState"/>
        </main>

        <section class="features">
            <div class="feature">
                <span class="feature-title">Fast</span>
                <img src="./assets/bolt.svg" class="icon">
                <p>Built using cutting-edge technology</p>
            </div>

            <div class="feature">
                <span class="feature-title">Secure</span>
                <img src="./assets/lock.svg" class="icon">
                <p>No logs, no anything</p>
            </div>
            
            <div class="feature">
                <span class="feature-title">Free</span>
                <img src="./assets/piggy-bank.svg" class="icon">
                <p>Absolutely no cost, for ever</p>
            </div>
        </section>

        <footer class="footer">
            <p>Made with &lt;3 by Sebastian Mendoza</p>
            <p class="small-text">Uicons by <a href="https://www.flaticon.com/uicons">Flaticon</a></p>
        </footer>
    </div>
</template>


<style scoped>
    .wrapper {
        display: flex;
        flex-direction: column;
        gap: 3rem;
    }

    .header, .footer {
        padding: 1em 0px;
        color: white;
    }

    .header {
        text-align: center;
        background-color: var(--primary-color);
    }

    .features {
        display: flex;
        justify-content: space-around;

        gap: 1em;
        padding: 1em;
    }

    .feature {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2em;

        flex: 1;

        text-align: center;
        padding: 1em;
    }

    .feature-title {
        font-weight: bold;
    }

    .icon {
        max-width: 5em;
    }

    .footer {
        display: flex;
        justify-content: space-between;

        background-color: var(--secondary-color);
        padding: 1em;
    }

    .small-text {
        font-size: smaller;
    }

    @media (max-width: 400px) {
        .features {
            flex-direction: column;
        }
    }
</style>

