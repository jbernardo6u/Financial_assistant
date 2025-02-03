import axios from 'axios';

const BASE_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
