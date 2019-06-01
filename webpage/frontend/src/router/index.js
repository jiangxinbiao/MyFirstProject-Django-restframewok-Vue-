import Vue from 'vue'
import mrouter from 'vue-router'
import content from '../components/content'
import foot from '../components/foot'
import header from '../components/header'
import Home from '../components/Home'
import hello from '../components/HelloWorld'

Vue.use(mrouter)

export default new mrouter({
  routes: [
      {
        path:'/header',
        name:'header',
        component:header,
      },
    {
      path:'/content',
      name:'content',
      component:content
    },
      {
        path:'/foot',
        name:'foot',
        component:foot
      },
      {
        path:'/',
        name:'Home',
        component:Home
      },
      {
        path:'/hello',
        name:'hello',
        component:hello
      },
  ]
})
