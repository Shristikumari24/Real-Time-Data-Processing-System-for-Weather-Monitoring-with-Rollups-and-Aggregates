import React from 'react';
import { List, ListItem, ListItemText, Typography } from '@material-ui/core';

const AlertList = ({ alerts }) => {
  return (
    <List>
      {alerts.map((alert, index) => (
        <ListItem key={index}>
          <ListItemText
            primary={alert.message}
            secondary={new Date(alert.timestamp).toLocaleString()}
          />
        </ListItem>
      ))}
    </List>
  );
};

export default AlertList;