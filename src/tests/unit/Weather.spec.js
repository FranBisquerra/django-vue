import {
  shallowMount
} from '@vue/test-utils'
import Weather from '@/components/Weather';
import {
  BASE_URL
} from "../../backend.js";


describe('Weather.vue testing', () => {

  const wrapper = shallowMount(Weather, {
    propsData: {
      city: 'Palma'
    }
  });

  it('Test initial state', () => {
    expect(wrapper.vm.error).toBe(undefined)
    expect(wrapper.vm.weatherForecast).toBe(undefined)
    expect(wrapper.vm.forecastUrl).toBe(`${BASE_URL}/api/forecast`)
  })
});
