import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
import Example from './Pages/Example'
import Test from './Pages/test'
class App extends Component {
  render() {
    return (
      <div className="App">
            <Example />
            <Test/>
      </div>
    );
  }
}

export default App;
