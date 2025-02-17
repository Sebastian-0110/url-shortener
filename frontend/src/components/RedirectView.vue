<script setup>
    import { watch } from "vue";
    import { useRouter, useRoute } from "vue-router";
    import endpoint from "@/api/endpoint.js";
    import { push } from "notivue";

    const router = useRouter();
    const route = useRoute();

    watch(() => route.params.urlCode, async () => {
        const response = await fetch(
            endpoint(`/urls/${route.params.urlCode}/details`),
            {
                method: "GET",
            },
        );
        const data = await response.json();

        if (!response.ok) {
            push.error(data.error);
            return await router.push({ name: "home" });
        }

        window.location.href = data["original_url"];

    }, { immediate: true });

</script>

<template>
    <div class="container vh-100 d-flex justify-content-center align-items-center">
        <div class="spinner-border"></div>
    </div>
</template>

<style scoped>

</style>