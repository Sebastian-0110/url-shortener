<script setup>
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    import endpoint from "@/api/endpoint.js";

    const url = ref("");
    const router = useRouter();

    async function submitForm() {
        const result = await fetch(endpoint("/urls/"), {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ url: url.value })
        });

        if (result.ok) {
            const data = await result.json();
            await router.push({
                name: "details",
                params: { urlCode: data["url_code"] }
            });
        }
    }
</script>

<template>
	<form action="/" method="post" class="d-flex flex-column align-items-center gap-3">
		<div class="container">
            <div class="row mb-4">
                <h3 class="text-center">Shorten your url</h3>
            </div>

            <div class="row justify-content-center align-items-center g-3">
                <div class="col col-12 col-sm-6">
                    <input
                        type="text"
                        v-model="url"
                        name="url"
                        id="url"
                        placeholder="Your url here"
                        class="form-control"
                    >
                </div>

                <div class="col col col-12 col-sm-2">
                    <input
                        type="submit"
                        id="submit"
                        value="Send"
                        @click.prevent="submitForm"
                        class="btn btn-primary w-100"
                    >
                </div>
            </div>
        </div>
    </form>
</template>

<style scoped>
</style>
