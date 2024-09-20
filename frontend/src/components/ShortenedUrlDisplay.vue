<script setup>	
	const props = defineProps({
		shortenedUrl: String,
		displayState: Object,
	});

	function handleClick() {
		props.displayState.show("form");
	}
</script>


<template>
	<div class="container">
		<p>Your url: {{ shortenedUrl }}</p>
		
		<button class="back" @click="handleClick">Back</button>
	</div>
</template>


<style scoped>
	.container {
		display: flex;
		flex-direction: column;
		align-items: center;

		gap: 1em;
	}

	.back {
		padding: 0.5em 1em;
	}

</style>