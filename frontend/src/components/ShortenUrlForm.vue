<script setup>
	import axios from "axios";
	import { ref } from "vue";

	const props = defineProps({
		displayState: Object,
	})

	const shortenedUrl = defineModel({ type: String });

	const url = ref("");
	// Change this to the actual endpoint
	const ENDPOINT = "http://localhost:5000/url/";

	function submitForm() {
		axios.post(
			ENDPOINT, 
			{ url: url.value },
			{ headers: {'content-type': 'multipart/form-data'} }
		)
			.then((response) => {
				shortenedUrl.value = response.data["shortened_url"];
				url.value = "";

				props.displayState.show("shortenedUrl");
			})

			.catch((error) => {
				props.displayState.show("errorMessage");
			});
	}
</script>


<template>
	<form action="/" method="post" class="form">
		<h3>Shorten your url</h3>

		<div class="inputs">
			<input type="text" name="url" id="url" class="url-input" placeholder="">
			<input type="submit" value="Ok"> 
		</div>
	</form>
</template>

<style scoped>
	.form {
		display: flex;
		flex-direction: column;
		gap: 1em;
	
		text-align: center;
	}

	.url-input {
		font-family: inherit;
		max-width: 90vw;
		padding: 0.5em;

		background-color: inherit;
		border: none;
		outline: 1px solid var(--secondary-color);
		border-radius: 0.5em;
	}

</style>
