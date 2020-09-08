import React from 'react';
import ReactDOM from 'react-dom';

import logo from './logo.svg';
import './App.css';
import {Route, BrowserRouter as Router, Switch, Link} from "react-router-dom";
import Login1 from './components/login1';
import Register from './components/register'
import Storage from './components/storage'
import OrderTaken from './components/ordertaken';
import Settings from './components/settings';
import CUSTOMER from './components/customer';
import Home from './components/home';
import CUSTEDIT from './components/customeredit';
import Employees from './components/Employees';
import Dashboard from './components/Dashboard';


function App() {

  return (
    <Router>
    <div className="App">
  
    <Switch>
         <Route path = "/" exact component = {Home} />
         <Route path="/login" exact component={Login1} />
         <Route path="/register" component={Register} />
         <Route path = "/ordertaken" component={() => <Settings pq={"true"} /> } />
         <Route path = "/setting" component={() => <Settings pq={"false"} /> } />
         <Route path = "/customer" component={CUSTOMER} />
         <Route path = "/customeredit" component={CUSTEDIT} />
         <Route path = "/employees" component={Employees} />
         <Route path = "/dashboard" component={Dashboard} />
    </Switch>
    </div>
    </Router>
  );
}

export default App;
