<script>
    import {HorizontalBar} from 'vue-chartjs';

    export default {
        name: 'bar-example',
        extends: HorizontalBar,
        props: ['budget', 'income', 'title', 'genre', 'release_date'],
        methods: {
            fillData(label, budget, income, genre, release_date) {
                this.datacollection = {
                    // Data for the y-axis of the chart
                    labels: label,
                    datasets: [
                        {
                            label: 'Budget',
                            backgroundColor: '#FF4136',
                            data: budget,
                            genres: genre,
                            release_date: release_date,
                        },
                        {
                            label: 'Income',
                            backgroundColor: '#2ECC40',
                            data: income,
                            genres: genre,
                            release_date: release_date,
                        },
                    ],
                }
            }
        },
        data: () => ({
            datacollection: null,
            options: {
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Value [$]',
                        },
                        stacked: false
                    }],
                    yAxes: [{
                        stacked: false,
                        scaleLabel: {
                            display: true,
                            labelString: 'Movie Title',
                        },
                    }]
                },
                tooltips: {
                  callbacks: {
                    label: function(tooltipItem, datacollection) {
                        var label = datacollection.datasets[tooltipItem.datasetIndex];
                        let element = [];
                        element.push(label.label + ' : ' + tooltipItem.value);
                        element.push('Title : ' + tooltipItem.label);
                        element.push('Genre: ' + label.genres[tooltipItem.index]);
                        element.push('Release Date: ' + label.release_date[tooltipItem.index]);
                        return element;
                    }
                  }
                },
                responsive: true,
                maintainAspectRatio: false,
            },
        }),
        mounted() {
            this.renderChart(this.datacollection, this.options);
        },
        watch: {
            budget() {
                this.fillData(this.title, this.budget, this.income, this.genre, this.release_date);
                this.renderChart(this.datacollection, this.options);
            },
            income() {
                this.fillData(this.title, this.budget, this.income, this.genre, this.release_date);
                this.renderChart(this.datacollection, this.options);
            }
        }
    };
</script>

<style>
</style>
