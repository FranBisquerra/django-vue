<template>
  <div>
    <div class="row">
      <div class="col-6 offset-3">
        <type-ahead v-model="city" :src="citiesUrl" :getResponse="getResponse"></type-ahead>
      </div>
    </div>
    <div class="row mt-3">
      <div class="col-10 offset-1">
        <div class="card">
          <div class="card-body">
            <div v-if="isValidCity">Victory</div>
            <div
              v-else
            >Weather forecast information is not available for the given city, please select one of the available ones.</div>
          </div>
        </div>
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
  computed: {
    isValidCity: function() {
      return this.cities.indexOf(this.city) !== -1;
    }
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
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.top-spacer {
  margin-top: 25px;
}
</style>
