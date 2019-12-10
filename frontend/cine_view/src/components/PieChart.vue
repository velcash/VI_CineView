<script>
import { Pie } from 'vue-chartjs';

export default {
  name: 'PieChart',
  extends: Pie,
  props: [ 'genres' , 'genreCount' ],
  data: () => ({
      datacollection: null,
      options: {
          title: {
              display: true,
              text: 'Genre distribution',
          },
          legend: {
            position: 'right',
          },
          tooltips: {
                  callbacks: {
                    label: function(tooltipItem, datacollection) {
                        var label = datacollection.datasets[tooltipItem.datasetIndex];
                        let sum = label.data.reduce((a,b) => a + b, 0);
                        let pourcentage = label.data[tooltipItem.index] * 100 / sum;
                        let element = '';
                        element += datacollection.labels[tooltipItem.index] + ' : ' + pourcentage + '%';
                        return element;
                    }
                  }
                },
      },
  }),
  methods: {
      fillData: function (g, gc) {
          this.datacollection = {
              datasets: [{
                data: gc,
                backgroundColor: ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9",
                    "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970",
                    "#111111", "#AAAAAA", "#10bb7c", "#cc9609",
                    "#8d17dd", "#ee0f5d"]
              }],
              labels: g,
          }
      }
  },
  watch: {
      genres () {
          this.fillData( this.genres, this.genreCount);
          this.renderChart(this.datacollection, this.options);
      },
      genreCount () {
          this.fillData( this.genres, this.genreCount);
          this.renderChart(this.datacollection, this.options);
      }
  },
  mounted() {
    this.renderChart(this.datacollection, this.options);
  },
};
</script>
