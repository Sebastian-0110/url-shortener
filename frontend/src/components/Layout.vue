<script setup>
    import Header from "./Header.vue";
    import Footer from "./Footer.vue";
</script>

<template>
    <div class="vh-100 d-flex flex-column gap-3">
        <Header />

        <main class="flex-grow-1 p-2 p-sm-4">
            <RouterView />
        </main>

        <Footer />
    </div>
</template>

<style scoped>
</style>

