<script setup>
	const props = defineProps({
		displayState: Object,
	});

	function handleClick() {
		props.displayState.show("form");
	}
</script>


<template>
	<div class="container">
		<p class="error-message">
			Error: The given url is not valid
		</p>

		<button class="try-another-url" @click="handleClick">Try another url</button>
	</div>

</template>

<style scoped>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;

		gap: 1em;
	}

	.try-another-url {
		padding: 0.5em 1em;
	}

</style>