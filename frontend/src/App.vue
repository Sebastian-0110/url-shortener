<script setup>
    import { Notivue, Notification, slateTheme } from 'notivue'
</script>

<template>
    <RouterView />

    <Notivue v-slot="item">
        <Notification :item="item" :theme="slateTheme" />
    </Notivue>
</template>

<style scoped>
</style>

