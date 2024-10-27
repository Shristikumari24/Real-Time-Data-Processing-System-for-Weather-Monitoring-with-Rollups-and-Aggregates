import React, { useState, useEffect } from 'react';
import { Typography } from '@material-ui/core';
import AlertList from '../components/AlertList';
import { fetchAlerts } from '../services/api';

const Alerts = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetchAlerts().then(setAlerts);
  }, []);

  return (
    <div>
      <Typography variant="h4" gutterBottom>Alerts</Typography>
      <AlertList alerts={alerts} />
    </div>
  );
};

export default Alerts;