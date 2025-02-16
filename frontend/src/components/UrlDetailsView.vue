<script setup>
    import {ref, watch, computed} from "vue";
    import { useRoute } from "vue-router";
    import endpoint from "@/api/endpoint.js";

    const route = useRoute();

    const originalUrl = ref("");
    const urlCode = ref("");

    const shortenedUrl = computed(() => `${location.host}/${urlCode.value}`);

    watch(() => route.params.uuid, async () => {
        const response = await fetch(
            endpoint(`/urls/${route.params.urlCode}/details`),
            { method: "GET" })
        ;

        if (response.ok) {
            const data = await response.json();

            originalUrl.value = data["original_url"];
            urlCode.value = data["url_code"];
        }
    }, { immediate: true });



</script>

<template>
	<div class="container">
        <p>Original url: {{ originalUrl }}</p>
        <p>Shortened url: {{ shortenedUrl }}</p>

        <RouterLink to="/">
            <button class="btn btn-primary">Go back</button>
        </RouterLink>
	</div>
</template>


<style scoped>

</style>