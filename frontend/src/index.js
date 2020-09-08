import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import  'bootstrap/dist/css/bootstrap.css';


//import 'bootstrap/3.4.1/css/bootstrap.min.css';
//import 'bootstrap/3.4.1/css/bootstrap-theme.min.css';
//import 'bootstrap/3.4.1/js/bootstrap.min.js';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
