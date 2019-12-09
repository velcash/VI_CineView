<template>
  <div class="container">
    <div class="row">
      <div class="col big-box">
        <bar-example :title="title" :budget="budget" :income="income"></bar-example>
      </div>
      <div class="col">
        <div class="row">
          <div class="col mini-box">
            <slider></slider>
          </div>
        </div>
        <div class="row">
          <div class="col mini-box">
            <div class="card">
              <article class="card-group-item">
                <header class="card-header">
                  <h6>Order By</h6>
                </header>
                <div class="form-check">
                  <div class="card-body">
                    <div class="form-check">
                      <label class="form-check-label">
                        <input type="radio"
                               class="form-check-input"
                               name="optradio"
                               v-on:change="getBudgetAscending">Ascending Budget
                      </label>
                    </div>
                    <div class="form-check">
                      <label class="form-check-label">
                        <input type="radio"
                               class="form-check-input"
                               name="optradio"
                               v-on:change="getBudgetDescending">Descending Budget
                      </label>
                    </div>
                    <div class="form-check">
                      <label class="form-check-label">
                        <input type="radio"
                               class="form-check-input"
                               name="optradio"
                               v-on:change="getIncomeAscending">Ascending Income
                      </label>
                    </div>
                    <div class="form-check">
                      <label class="form-check-label">
                        <input type="radio"
                               class="form-check-input"
                               name="optradio"
                               checked
                               v-on:change="getIncomeDescending">Descending Income
                      </label>
                    </div>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col mini-box">
            <div class="card">
              <article class="card-group-item">
                <header class="card-header">
                  <h6>Filter By</h6>
                </header>
                <div class="form-check">
                  <div class="card-body">
                    <form>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" v-on:change="filterByOscars">
                        <span class="form-check-label">
                          Oscars
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" v-on:change="filterByPalme">
                        <span class="form-check-label">
                          Palme d'or
                        </span>
                      </label>
                    </form>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col mini-box">
            <pie-chart :genres="genre" :genre-count="genreCount"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BarExample from './BarExample.vue';
import PieChart from './PieChart.vue';
import Slider from './Slider.vue';
import axios from 'axios';

export default {
  components: { BarExample, Slider, PieChart },

  data: function() {
    return {
        orderState: 'ba',
        filterPalme: false,
        filterOscars: false,
        boxOffices: [],
        budget: [],
        income: [],
        title: [],
        genre: [],
        genreCount: [],
    }
  },

  methods: {
    getBudgetAscending: function() {
      this.orderState = 'ba';
      const path = 'http://localhost:5000/budgetAscending';
      axios.get(path)
        .then((res) => {
          this.boxOffices = res.data.json_list;
          this.parseBudget();
          this.parseIncome();
          this.parseTitle();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getBudgetDescending: function() {
      this.orderState = 'bd';
      const path = 'http://localhost:5000/budgetDescending';
      axios.get(path)
        .then((res) => {
          this.boxOffices = res.data.json_list;
          this.parseBudget();
          this.parseIncome();
          this.parseTitle();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getIncomeAscending: function() {
      this.orderState = 'ia';
      const path = 'http://localhost:5000/incomeAscending';
      axios.get(path)
        .then((res) => {
          this.boxOffices = res.data.json_list;
          this.parseBudget();
          this.parseIncome();
          this.parseTitle();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getIncomeDescending: function() {
      this.orderState = 'id';
      const path = 'http://localhost:5000/incomeDescending';
      axios.get(path)
        .then((res) => {
          this.boxOffices = res.data.json_list;
          this.parseBudget();
          this.parseIncome();
          this.parseTitle();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getGenre: function() {
        const path = 'http://localhost:5000/getGenre';
        axios.get(path)
          .then((res) => {
            for (let [key, value] of Object.entries(res.data.json_list)) {
                this.genreCount.push(value);
                this.genre.push(key);
            }
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    },
    filterByOscars: function() {
        this.filterOscars = !this.filterOscars;
        console.log(this.filterOscars);
    },
    filterByPalme: function() {
        this.filterPalme = !this.filterPalme;
        console.log(this.filterPalme);
    },
    parseBudget: function() {
        this.budget = [];
        this.boxOffices.forEach(element => this.budget.push(element.budget));
    },
      parseIncome: function() {
        this.income = [];
        this.boxOffices.forEach(element => this.income.push(element.revenue));
    },
    parseTitle: function() {
        this.title = [];
        this.boxOffices.forEach(element => this.title.push(element.title));
    }
  },
  created() {
    this.getIncomeDescending();
    this.getGenre();
  },
};
</script>

<style>
</style>
