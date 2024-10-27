import axios from 'axios';

const API_URL = 'http://localhost:5000/api'; // Adjust this to your backend URL

export const fetchWeatherData = async () => {
  const response = await axios.get(`${API_URL}/weather`);
  return response.data;
};

export const fetchTemperatureData = async () => {
  const response = await axios.get(`${API_URL}/temperature`);
  return response.data;
};

export const fetchAlerts = async () => {
  const response = await axios.get(`${API_URL}/alerts`);
  return response.data;
};