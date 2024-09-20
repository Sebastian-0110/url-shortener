<script setup>
	import { postRequest } from "../logic/postRequest"
	import { ref } from "vue";

	const props = defineProps({
		displayState: Object,
	})

	const url = ref("");
	const shortenedUrl = defineModel({ type: String });

	async function submitForm() {
		const { response, error } = await postRequest(
			"https://urlshortener.pythonanywhere.com/url/",
			{ url: url.value },
			{ headers: {'content-type': 'multipart/form-data'} }
		)

		if (response) {
			shortenedUrl.value = response["shortened_url"];
			props.displayState.show("shortenedUrl");
			url.value = "";
		}

		if (error) {
			props.displayState.show("errorMessage");
		}
	}
</script>


<template>
	<form action="/" method="post" class="form">
		<h3>Shorten your url</h3>

		<div class="inputs">
			<input type="text" v-model="url" name="url" id="url" class="url-input" placeholder="">
			<input type="submit" class="submit-button" id="submit" value="Ok" @click.prevent="submitForm"> 
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
		
		width: 30em;
		max-width: 70%;

		background-color: inherit;
		border: none;
		outline: 1px solid var(--secondary-color);
		border-radius: 0.5em;
	}

	.inputs {
		display: flex;
		justify-content: center;
		gap: 1em;
	}

	.submit-button {
		padding: 0.5em 1.5em;
	}

</style>
