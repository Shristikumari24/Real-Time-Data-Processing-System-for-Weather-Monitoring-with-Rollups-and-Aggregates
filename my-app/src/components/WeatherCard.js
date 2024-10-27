import React from 'react';
import { Card, CardContent, Typography } from '@material-ui/core';

const WeatherCard = ({ city, temperature, condition }) => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" component="h2">
          {city}
        </Typography>
        <Typography color="textSecondary">
          {condition}
        </Typography>
        <Typography variant="body2" component="p">
          Temperature: {temperature}°C
        </Typography>
      </CardContent>
    </Card>
  );
};

export default WeatherCard;