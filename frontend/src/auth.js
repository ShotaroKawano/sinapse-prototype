import axios from 'axios'

const axiosAuth = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  // baseURL: 'https://sinapse-20201015.herokuapp.com/',
})

export default axiosAuth;
