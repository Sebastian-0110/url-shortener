<script setup>
    import { Notivue, Notification, slateTheme } from 'notivue'

    import Header from "./components/Header.vue";
    import Footer from "./components/Footer.vue";
</script>

<template>
    <div class="vh-100 d-flex flex-column gap-3">
        <Header />

        <main class="flex-grow-1 p-2 p-sm-4">
            <RouterView />
        </main>

        <Footer />
    </div>

    <Notivue v-slot="item">
        <Notification :item="item" :theme="slateTheme" />
    </Notivue>
</template>

<style scoped>
</style>

