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
	<div class="container pt-5 text-center">
        <div class="row mb-3">
            <h3>Your shortened url:</h3>
        </div>

        <div class="row justify-content-center gy-2">
            <div class="col col-12 col-sm-6">
                <input class="form-control form-control-lg" :value="shortenedUrl" />
            </div>

            <div class="col col-12 col-sm-auto">
                <button class="btn btn-primary btn-lg w-100">Copy</button>
            </div>
        </div>

        <div>
            <p class="form-text mt-2 mb-5">This url takes you to: {{ originalUrl }}</p>
        </div>

        <RouterLink to="/">
            <button class="btn btn-primary btn-lg">Go back</button>
        </RouterLink>
	</div>
</template>


<style scoped>

</style>