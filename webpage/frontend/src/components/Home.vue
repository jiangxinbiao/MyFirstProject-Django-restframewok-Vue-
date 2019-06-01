<!--1模板：html结构-->

<template>
  <div id="ahome">
    <!--<p>这是主页</p>-->
    <AHeader></AHeader>
    <AContent v-bind:txt="categoryList"></AContent>
    <AFooter></AFooter>
  </div>
</template>

<script>
  import footer from './foot'
  import header from './header'
  import content from './content'
  export default {
    name: 'ahome',
    created(){
      this.getCategory();
    },
    data(){
      return{
        categoryList:[]
      }
    },
    components: {
      'AFooter': footer,
      'AHeader': header,
      'AContent': content,
    },
    // created:{
    //   this.$axios.get("http://jsonplaceholder.typicode.com/users")
    //     .then(function (response) {
    //       console.log(response.data);
    //       this.users = response.data.body
    //     })
    //     .catch(function (error) {
    //       console.log(error);
    //     })
    // }

    //http://localhost:8000/user/Userlist/      "http://jsonplaceholder.typicode.com/users"
    methods:{
      getCategory:function(){
        this.$axios.get("http://localhost:8000/user/Userlist/").then( res =>{
          this.categoryList = res.data;
          console.log(res.data)
          }
        )
      }
    }
  }
</script>

<!--3样式：解决样式-->
<style>
  #home {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    position: relative;
  }
  h1,h2{
    color: #1d0b1d;
  }
  ul{
    color: #1d0b1d;
  }
</style>
