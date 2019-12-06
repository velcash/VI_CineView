<script>
import { HorizontalBar } from 'vue-chartjs';

export default {
  name: 'bar-example',
  extends: HorizontalBar,
  data: () => ({
    chartdata: {
      labels: ['January', 'February', 'March', 'April', ' May'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [10, 20, 30, 40, 50],
        },
        {
          label: 'Data Two',
          backgroundColor: '#74992e',
          data: [10, 20, 30, 40, 50],
        },
      ],
    },
    options: {
        scales: {
            xAxes: [{
                stacked: true
            }],
            yAxes: [{
                stacked: true
            }]
        },
        responsive: true,
        maintainAspectRatio: false,
    },
  }),
  mounted() {
    this.renderChart(this.chartdata, this.options);
  },
};
</script>

<style>
</style>
