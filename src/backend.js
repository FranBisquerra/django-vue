import axios from 'axios'
import Cookies from 'js-cookie'

export const BASE_URL = 'http://localhost:8000'

let $backend = axios.create({
  baseURL: `${BASE_URL}/api`,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken')
  }
})

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
});

$backend.$fetchForecast = (city) => {
  return $backend.get(`forecast`, {
    params: {
      city: city
    }
  })
}

$backend.$fetchCities = () => {
  return $backend.get(`cities`)
}

export default $backend
