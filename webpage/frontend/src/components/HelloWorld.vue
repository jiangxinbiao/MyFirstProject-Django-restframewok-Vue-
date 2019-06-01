<!--html框架-->
<template>
  <div class="hello">
    {{msg}}
  </div>
</template>

<!--逻辑-->
<script>
export default {
  name:'hello',
  data(){
    return{
      msg:'这是你好世界页面'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

<!--样式-->
<style scoped>

</style>
