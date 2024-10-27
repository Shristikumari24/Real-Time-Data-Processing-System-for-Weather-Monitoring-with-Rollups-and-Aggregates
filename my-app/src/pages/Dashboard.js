import React, { useState, useEffect } from 'react';
import { Grid, Typography } from '@material-ui/core';
import WeatherCard from '../components/WeatherCard';
import TemperatureChart from '../components/TemperatureChart';
import { fetchWeatherData, fetchTemperatureData } from '../services/api';

const Dashboard = () => {
  const [weatherData, setWeatherData] = useState([]);
  const [temperatureData, setTemperatureData] = useState([]);

  useEffect(() => {
    fetchWeatherData().then(setWeatherData);
    fetchTemperatureData().then(setTemperatureData);
  }, []);

  return (
    <div>
      <Typography variant="h4" gutterBottom>Dashboard</Typography>
      <Grid container spacing={3}>
        {weatherData.map(city => (
          <Grid item xs={12} sm={6} md={4} key={city.name}>
            <WeatherCard
              city={city.name}
              temperature={city.temperature}
              condition={city.condition}
            />
          </Grid>
        ))}
      </Grid>
      <Typography variant="h5" gutterBottom style={{ marginTop: '2rem' }}>Temperature Trends</Typography>
      <TemperatureChart data={temperatureData} />
    </div>
  );
};

export default Dashboard;