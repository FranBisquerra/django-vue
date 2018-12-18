import {
  shallowMount
} from '@vue/test-utils'
import Forecast from '@/components/Forecast';
import {
  BASE_URL
} from "../../backend.js";


describe('Forecast.vue testing', () => {

  const wrapper = shallowMount(Forecast);

  it('Test initial state, the sentence asking the user to type in a city.', () => {
    expect(wrapper.vm.city).toBe("")
    expect(wrapper.vm.cities).toEqual([])
    expect(wrapper.vm.citiesUrl).toBe(`${BASE_URL}/api/cities`)
    expect(wrapper.vm.isValidCity).toBe(false)
    expect(wrapper.text()).toContain("Weather forecast information")

  })

  it('Test Select a city, once a city is selected the weather component with the city attr is displayed', () => {
    wrapper.setData({
      city: 'Palma',
      cities: ['Palma']
    })
    expect(wrapper.vm.city).toBe("Palma")
    expect(wrapper.vm.cities).toEqual(['Palma'])
    expect(wrapper.vm.isValidCity).toBe(true)
    expect(wrapper.html()).toContain('<weather-stub city="Palma">')
  })
});
