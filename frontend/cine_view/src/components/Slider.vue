<script>
import VueSlider from 'vue-slider-component';

import 'vue-slider-component/theme/default.css';

export default {
  name: 'slider',
  extends: VueSlider,

  data: function () {
    return {
      value2: [2010, 2019],
    };
  },
};
</script>
