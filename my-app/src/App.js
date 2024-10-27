// import React from 'react';
const React = require('react');

import { BrowserRouter as Router,  Route ,Switch} from 'react-router-dom';
import { Container } from '@material-ui/core';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import Alerts from './pages/Alerts';

function App() {
  return (
    <Router>
      <Switch>
      <div className="App">
        <Header />
        <Container style={{ marginTop: '2rem', marginBottom: '2rem' }}>
          <Switch>
            <Route exact path="/" component={Dashboard} />
            <Route path="/alerts" component={Alerts} />
          </Switch>
        </Container>
        <Footer />
      </div>
      </Switch>
    </Router>
  );
}

export default App;