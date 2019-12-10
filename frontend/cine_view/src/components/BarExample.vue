<script>
    import {HorizontalBar} from 'vue-chartjs';

    export default {
        name: 'bar-example',
        extends: HorizontalBar,
        props: ['budget', 'income', 'title'],
        methods: {
            fillData(label, budget, income) {
                this.datacollection = {
                    // Data for the y-axis of the chart
                    labels: label,
                    datasets: [
                        {
                            label: 'Budget',
                            backgroundColor: '#f87979',
                            data: budget,
                        },
                        {
                            label: 'Income',
                            backgroundColor: '#74992e',
                            data: income,
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
                            labelString: 'Title',
                        },
                    }]
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
                this.fillData(this.title, this.budget, this.income);
                this.renderChart(this.datacollection, this.options);
            },
            income() {
                this.fillData(this.title, this.budget, this.income);
                this.renderChart(this.datacollection, this.options);
            }
        }
    };
</script>

<style>
</style>
