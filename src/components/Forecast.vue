<template>
  <div>
    <div class="row">
      <div class="col-5 offset-3">
        <type-ahead v-model="city" :src="citiesUrl" :getResponse="getResponse"></type-ahead>
      </div>
      <div class="col-1">
        <button type="button" class="btn btn-primary" v-on:click="fetchForecast()">Search</button>
      </div>
    </div>
  </div>
</template>

<script>
import { BASE_URL } from "../backend.js";
import TypeAhead from "vue2-typeahead";

export default {
  name: "Forecast",
  data() {
    return {
      cities: [],
      city: "",
      citiesUrl: `${BASE_URL}/api/cities`
    };
  },
  mounted: function() {
    this.baseUrl = BASE_URL;
  },
  components: {
    "type-ahead": TypeAhead
  },
  methods: {
    getResponse(response) {
      this.cities = response.data;
      return response.data;
    },
    fetchForecast() {}
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
