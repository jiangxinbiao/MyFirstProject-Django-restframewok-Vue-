// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue';
import App from './App';
import router from './router';
import Vuerouter from 'vue-router';
import axios from 'axios';
// import VueAxios from 'vue-axios'

Vue.prototype.$axios = axios;
Vue.use(Vuerouter)

// Vue.prototype.$http=axiosVue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  components: { App },
  template: '<App/>'
})

