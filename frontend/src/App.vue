<template>
  <div id="app">
    <Nav />
    <router-view />
    <Footer />
  </div>
</template>
<style>
</style>
<script>

import Nav from "./components/nav";
import Footer from "./components/footer";
export default { components: { Nav, Footer }};
</script>
