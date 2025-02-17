<script setup>
    import { ref, watch, computed } from "vue";
    import { useRouter, useRoute } from "vue-router";
    import { push } from "notivue";
    import endpoint from "@/api/endpoint.js";

    const router = useRouter();
    const route = useRoute();

    const originalUrl = ref("");
    const urlCode = ref("");
    const isFetching = ref(false);

    const shortenedUrl = computed(() => `${location.origin}/${urlCode.value}`);

    watch(() => route.params.uuid, async () => {
        isFetching.value = true;
        const response = await fetch(
            endpoint(`/urls/${route.params.urlCode}/details`),
            { method: "GET" }
        );
        const data = await response.json();

        if (!response.ok) {
            push.error(data.error);
            return await router.push({ name: "home" });
        }

        originalUrl.value = data["original_url"];
        urlCode.value = data["url_code"];
        isFetching.value = false;
    }, { immediate: true });

    async function copyToClipboard() {
        await navigator.clipboard.writeText(shortenedUrl.value);
        push.success("Copied to the clipboard")
    }

</script>

<template>
	<div class="container pt-5 text-center">
        <div class="row mb-3">
            <h3>Your shortened url:</h3>
        </div>

        <div class="row justify-content-center gy-2">
            <div class="col col-12 col-sm-6">
                <span class="form-control form-control-lg text-start">
                    <span v-if="isFetching" class="placeholder placeholder-wave col-12 rounded"></span>
                    <span v-else>{{ shortenedUrl }}</span>
                </span>
            </div>

            <div class="col col-12 col-sm-auto">
                <button
                    class="btn btn-primary btn-lg w-100"
                    @click="copyToClipboard"
                    :disabled="isFetching"
                >Copy</button>
            </div>
        </div>

        <div>
            <p class="form-text mt-2 mb-5">
                This url takes you to:
                <span v-if="isFetching" class="placeholder placeholder-wave col-3 rounded"></span>
                <span v-else>{{ originalUrl }}</span>
            </p>
        </div>

        <RouterLink to="/">
            <button class="btn btn-primary btn-lg">Go back</button>
        </RouterLink>
	</div>
</template>


<style scoped>

</style>