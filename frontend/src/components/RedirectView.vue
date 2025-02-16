<script setup>
    import { watch } from "vue";
    import { useRoute } from "vue-router";
    import endpoint from "@/api/endpoint.js";

    const route = useRoute();

    watch(() => route.params.urlCode, async () => {
        const response = await fetch(
            endpoint(`/urls/${route.params.urlCode}/details`),
            {
                method: "GET",
            },
        );

        if (response.ok) {
            const data = await response.json();
            window.location.href = data["original_url"];
        }

    }, { immediate: true });

</script>

<template>

</template>

<style scoped>

</style>