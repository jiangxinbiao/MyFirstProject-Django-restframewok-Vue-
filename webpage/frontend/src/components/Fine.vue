<template>
    <div class="fine">
      <h1>{{msg}}</h1>
      <p>{{p1}}</p>
      <!--<ul>-->
        <!--<li v-for="user in users" v-on:click="user.show = !user.show">-->
            <!--<h2>{{user.name}}</h2>-->
          <!--<h3 v-show="user.show">{{user.position}}</h3>-->
        <!--</li>-->
      <!--</ul>-->
    </div>
</template>

<script>
    export default {
        name: "fine1",
        data(){
          return{
            msg:"老李你好",
            p1:"老李你胖",
            users:[
                    {name:"asd",position:"吃大葱",show:false},
                    {name:"asd",position:"吃大葱",show:false},
                    {name:"xc",position:"吃大葱",show:false},
                    {name:"asd",position:"吃大葱",show:false},
                    {name:"xrg",position:"吃大葱",show:false},
                    {name:"fgh",position:"吃大葱",show:false},
                    {name:"cv",position:"吃大葱",show:false},
                    {name:"a",position:"吃大葱",show:false},
                    {name:"xfcae",position:"吃大葱",show:false},
                    {name:"cxv",position:"吃大葱",show:false},
                    {name:"xc",position:"吃大葱",show:false},
                  ]
          }
        }
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
