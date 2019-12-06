import Vue from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import VueSlider from 'vue-slider-component';
import 'vue-slider-component/theme/default.css';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faUserSecret } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import App from './App.vue';
import router from './router';

Vue.config.productionTip = false;
library.add(faUserSecret);
Vue.component('VueSlider', VueSlider);
Vue.component('font-awesome-icon', FontAwesomeIcon);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
