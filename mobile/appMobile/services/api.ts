import axios from 'axios';

const api = axios.create({
  baseURL: 'https://ncr19qt9xd.execute-api.us-east-1.amazonaws.com',
});

export default api;
