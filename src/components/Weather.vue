<template>
  <div>
    <div class="card">
      <div class="card-body">
        <div v-if="weatherForecast">
          <div class="row">
            <div class="col">
              <img
                class="rounded"
                :src="require(`@/assets/${weatherForecast.weather[0].icon}.png`)"
              >
            </div>
            <div class="col">
              <div class="row">
                <h1>Temp:{{weatherForecast.main.temp}}</h1>
              </div>
              <div class="row">
                <p>{{weatherForecast.weather[0].main}}: {{weatherForecast.weather[0].description}}</p>
              </div>
            </div>
          </div>
        </div>
        <div v-if="error">
            <p> Unnexpected error: {{error}} please contact our support center.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { BASE_URL } from "../backend.js";

export default {
  name: "Weather",
  props: {
    city: String
  },
  data() {
    return {
      forecastUrl: `${BASE_URL}/api/forecast`,
      weatherForecast: undefined,
      error: undefined
    };
  },
  watch: {
    city: {
      immediate: true,
      handler(val, oldVal) {
        if (val !== oldVal) {
          this.fetchForecast(val);
        }
      }
    }
  },
  methods: {
    fetchForecast(city) {
      this.$backend.$fetchForecast(city).then(rs => {
        this.weatherForecast = rs.data;
        this.error = undefined;
      }).catch(rs => {
          this.error= rs.message;
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
