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
                <span>Fast</span>
                <p>Lorem ipsum dolor sit amet consectetur</p>
            </div>

            <div class="feature">
                <span>Secure</span>
                <p>Lorem ipsum dolor sit amet consectetur</p>
            </div>
            
            <div class="feature">
                <span>Free</span>
                <p>Lorem ipsum dolor sit amet consectetur</p>
            </div>
        </section>

        <footer class="footer">
            <p>Made with &lt;3 by Sebastian Mendoza</p>
        </footer>
    </div>
</template>


<style scoped>
    .wrapper {
        display: flex;
        flex-direction: column;
        gap: 4rem;
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
        outline: 1px solid black;
        text-align: center;
        padding: 3em 1em;
    }

    .footer {
        background-color: var(--secondary-color);
    }

    @media (max-width: 250px) {
        .features {
            flex-wrap: wrap;
        }
    }
</style>

