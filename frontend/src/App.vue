<template>
  <cabecera></cabecera>
  <router-view></router-view>
</template>

<script>
import Cabecera from "./components/layouts/Cabecera";

export default {
  components: {
    Cabecera
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap");

* {
  box-sizing: border-box;
}

html {
  font-family: "Roboto", sans-serif;
}

body {
  margin: 0;
}
</style>
