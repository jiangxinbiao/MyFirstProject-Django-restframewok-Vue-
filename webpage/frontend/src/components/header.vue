<<!--html框架-->
<template>
  <div class="aheader">
    <h2>{{tatle}}</h2>
    <router-link to="/content"><h3>主页内容</h3></router-link>
  </div>
</template>

<!--逻辑-->
<script>
  export default {
    name:'aheader',
    data(){
      return{
        tatle:'江汉的博客'
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<!--样式-->
<style scoped>
.aheader{
  padding: 10px;
  background: 20px #633535;
}
h2{
    color:#e2ddff;
  }
h3{

  text-align: justify;
  color: #f4ffed;
}
</style>

