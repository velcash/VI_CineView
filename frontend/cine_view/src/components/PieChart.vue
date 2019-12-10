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
      },
  }),
  methods: {
      fillData: function (g, gc) {
          this.datacollection = {
              datasets: [{
                data: gc,
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
