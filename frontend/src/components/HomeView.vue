<script setup>
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    import endpoint from "@/api/endpoint.js";
    import {push} from "notivue";

    const url = ref("");
    const router = useRouter();

    async function submitForm() {
        if (url.value === "") {
            return push.warning("Please enter a valid url");
        }

        const result = await fetch(endpoint("/urls/"), {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ url: url.value })
        });
        const data = await result.json();

        if (!result.ok)
            return push.error(data.error)

        await router.push({
            name: "details",
            params: { urlCode: data["url_code"] }
        });
    }
</script>

<template>
	<form action="/" method="post" class="d-flex flex-column align-items-center gap-3 pt-5">
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
                        class="form-control form-control-lg"
                        required
                    >
                </div>

                <div class="col col col-12 col-sm-2">
                    <input
                        type="submit"
                        id="submit"
                        value="Send"
                        @click.prevent="submitForm"
                        class="btn btn-primary btn-lg w-100"
                    >
                </div>
            </div>
        </div>
    </form>
</template>

<style scoped>
</style>
