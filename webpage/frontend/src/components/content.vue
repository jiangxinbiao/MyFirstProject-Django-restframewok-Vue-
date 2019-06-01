<template>
  <div class="fine1">
    <h2></h2>
      <div>
        <h1 v-for="user in txt">
          {{user.username}}
        </h1>
      </div>
  </div>
</template>

<script>
  export default {
    name: "fine1",
    data(){
      return{
      }
    },
    props:["txt"]
  }
</script>

<style scoped>
  h1,h2{
    color: aqua;
  }
  ul{
    color: brown;
  }
</style>
