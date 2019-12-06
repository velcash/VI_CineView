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
                    <form>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
                        <span class="form-check-label">
                          Ascending Budget
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
                        <span class="form-check-label">
                          Descending Budget
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
                        <span class="form-check-label">
                          Ascending Income
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
                        <span class="form-check-label">
                          Descending Income
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
            <div class="card">
              <article class="card-group-item">
                <header class="card-header">
                  <h6>Filter By</h6>
                </header>
                <div class="form-check">
                  <div class="card-body">
                    <form>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
                        <span class="form-check-label">
                          Oscars
                        </span>
                      </label>
                      <label class="form-check">
                        <input class="form-check-input" type="checkbox" value="">
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
};
</script>

<style>
</style>
