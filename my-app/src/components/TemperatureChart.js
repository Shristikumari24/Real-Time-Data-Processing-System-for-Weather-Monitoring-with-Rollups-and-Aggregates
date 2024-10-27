import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const TemperatureChart = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="avgTemp" stroke="#8884d8" name="Average Temp" />
        <Line type="monotone" dataKey="maxTemp" stroke="#82ca9d" name="Max Temp" />
        <Line type="monotone" dataKey="minTemp" stroke="#ffc658" name="Min Temp" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default TemperatureChart;