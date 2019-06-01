<<!--html框架-->
<template>
  <div class="afooter">
    <h1>{{tatle}}</h1>
  </div>
</template>

<!--逻辑-->
<script>
  export default {
    name:'afooter',
    data(){
      return{
        tatle:'这是页面底部'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<!--样式-->
<style scoped>
  .afooter{
    padding:6px;
    background: 20px #633535;

  }
  h1{
    color:#e2ddff;
    text-align: center;
  }
</style>
头部（Header.vue）
