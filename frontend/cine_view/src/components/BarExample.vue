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
                            backgroundColor: '#FF4136',
                            data: budget,
                        },
                        {
                            label: 'Income',
                            backgroundColor: '#2ECC40',
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
