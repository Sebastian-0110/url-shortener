<script setup>
</script>


<template>
	<div class="container">
		<p>Your url: {{ $route.params.url_code }}</p>
		
        <RouterLink to="/">
            <button class="btn btn-primary">Go back</button>
        </RouterLink>
	</div>
</template>


<style scoped>

</style>