<template>
  <div id="app">
    {{ Title }}
    <file-upload></file-upload>
  </div>
</template>

<script>
import FileUpload from './components/FileUpload'
export default {
  components: { FileUpload},
  name: 'App',
  data () {
    return {
      Title: process.env.VUE_APP_TITLE
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
