<script>
import { Pie } from 'vue-chartjs';

export default {
  name: 'PieChart',
  extends: Pie,
  data: () => ({
    chartdata: {
      datasets: [{
        backgroundColor: ['#f87979', '#74992e', '#74992e'],
        data: [10, 20, 30],
      }],
      labels: [
        'Red',
        'Yellow',
        'Blue',
      ],
    },
    options: {},
  }),
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>
