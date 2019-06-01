<!--1模板：html结构-->

<template>
  <div id="app">
    <!--<div class="navbottom">-->
    <router-link to="/Home"></router-link>
    <!--</div>-->
      <!--<div class="navbottom">-->
    <router-link to="/content"></router-link>
      <!--</div>-->

      <router-view></router-view>

  </div>
</template>

<!--2行为：处理逻辑-->
<script>
export default {
  name:'app',
}
</script>

<!--3样式：解决样式-->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  position: relative;
}

</style>
