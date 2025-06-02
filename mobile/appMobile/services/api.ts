import axios from 'axios';

const api = axios.create({
  baseURL: 'https://ydsdpxj25l.execute-api.us-east-1.amazonaws.com',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
