<template>
  <div class="container">
    <div class="row">
      <div class="col big-box">
        <bar-example></bar-example>
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
            <pie-chart/>
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

export default {
  components: { BarExample, Slider, PieChart },

  data: function() {
    return {
        orderState: 'ba',
        filterPalme: false,
        filterOscars: false,
    }
  },

  methods: {
    getBudgetAscending: function() {
      this.orderState = 'ba';
      console.log(this.orderState);
    },
    getBudgetDescending: function() {
      this.orderState = 'bd';
      console.log(this.orderState);
    },
    getIncomeAscending: function() {
      this.orderState = 'ia';
      console.log(this.orderState);
    },
    getIncomeDescending: function() {
      this.orderState = 'id';
      console.log(this.orderState);
    },
    filterByOscars: function() {
        this.filterOscars = !this.filterOscars;
        console.log(this.filterOscars);
    },
    filterByPalme: function() {
        this.filterPalme = !this.filterPalme;
        console.log(this.filterPalme);
    }
  },
};
</script>

<style>
</style>
