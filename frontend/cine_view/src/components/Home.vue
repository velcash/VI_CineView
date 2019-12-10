<template>
  <div class="container">
    <div class="row">
      <div class="col big-box">
        <bar-example :title="title" :budget="budget" :income="income"></bar-example>
      </div>
      <div class="col">
        <div class="row" style="margin-bottom: 30px">
          <div class="col mini-box">
            <span>Years filtering</span>
            <vue-slider v-model="value" :data="data" :marks="true" :order="false"></vue-slider>
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
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">
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
                    </li>
                    <li class="list-group-item">
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" v-on:change="filterByUsa">
                        <span class="form-check-label">
                          USA
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" v-on:change="filterByOthers">
                        <span class="form-check-label">
                          Other Countries
                        </span>
                      </label>
                    </li>
                  </ul>
              </article>
            </div>
          </div>
        </div>
       </div>
    </div>
    <div class="row">
      <div class="col-3">
        <span></span>
      </div>
      <div class="col-6">
        <pie-chart :genres="genre" :genre-count="genreCount"/>
      </div>
    </div>
    <div class="col-3">
        <span></span>
    </div>
  </div>
</template>

<script>
import BarExample from './BarExample.vue';
import PieChart from './PieChart.vue';
import VueSlider from 'vue-slider-component';
import 'vue-slider-component/theme/default.css';
import axios from 'axios';

export default {
  components: { BarExample, VueSlider, PieChart },

  data: function() {
    return {
        orderState: 'ba',
        filterPalme: false,
        filterOscars: false,
        filterUsa: false,
        filterOthers: false,
        startDate: '2008',
        endDate: '2016',
        boxOffices: [],
        budget: [],
        income: [],
        title: [],
        genre: [],
        genreCount: [],
        value: [2008, 2016],
        data: [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
    }
  },

  methods: {
    getBudgetAscending: function() {
      this.orderState = 'ba';
      const path = 'http://localhost:5000/budgetAscending';
      axios.post(path, {
            palme: this.filterPalme,
            oscar: this.filterOscars,
            usa: this.filterUsa,
            others: this.filterOthers,
            startDate: this.startDate,
            endDate: this.endDate,
        })
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
      axios.post(path, {
            palme: this.filterPalme,
            oscar: this.filterOscars,
            usa: this.filterUsa,
            others: this.filterOthers,
            startDate: this.startDate,
            endDate: this.endDate,
        })
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
      axios.post(path, {
            palme: this.filterPalme,
            oscar: this.filterOscars,
            usa: this.filterUsa,
            others: this.filterOthers,
            startDate: this.startDate,
            endDate: this.endDate,
        })
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
      axios.post(path, {
            palme: this.filterPalme,
            oscar: this.filterOscars,
            usa: this.filterUsa,
            others: this.filterOthers,
            startDate: this.startDate,
            endDate: this.endDate,
        })
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
        this.getFilters(this.orderState, this.filterPalme, this.filterOscars, this.filterUsa, this.filterOthers, this.startDate, this.endDate);
    },
    filterByPalme: function() {
        this.filterPalme = !this.filterPalme;
        this.getFilters(this.orderState, this.filterPalme, this.filterOscars, this.filterUsa, this.filterOthers, this.startDate, this.endDate);
    },
    filterByUsa: function() {
        this.filterUsa = !this.filterUsa;
        this.getFilters(this.orderState, this.filterPalme, this.filterOscars, this.filterUsa, this.filterOthers, this.startDate, this.endDate);
    },
    filterByOthers: function() {
        this.filterOthers = !this.filterOthers;
        this.getFilters(this.orderState, this.filterPalme, this.filterOscars, this.filterUsa, this.filterOthers, this.startDate, this.endDate);
    },
    getFilters: function(type, palme, oscar, usa, others, startDate, endDate) {
        const path = 'http://localhost:5000/getFilterByRec';
        axios.post(path, {
            type: type,
            palme: palme,
            oscar: oscar,
            usa: usa,
            others: others,
            startDate: startDate,
            endDate: endDate,
        })
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
    },
    getHome: function() {
      this.orderState = 'id';
      const path = 'http://localhost:5000/';
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
    }
  },
  created() {
    this.getHome();
    this.getGenre();
  },
  watch: {
      value() {
        this.value.sort((a, b) => a - b);
        this.startDate = this.value[0];
        this.endDate = this.value[1];
        this.getFilters(this.orderState, this.filterPalme, this.filterOscars, this.filterUsa, this.filterOthers, this.startDate, this.endDate);
      }
  }
};
</script>

<style>
</style>
