import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
//import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Sidebar from './layouts/Sidebar';
import Dashboard from './components/Dashboard';
import AddCompany from './pages/AddCompany';
import AnalyzeData from './pages/AnalyzeData';
import ViewGraphs from './pages/ViewGraphs';
import FetchData from './pages/FetchData';
import Settings from './pages/Settings';


const App = () => {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route exact path="/" component={Dashboard} />
            <Route path="/add-company" component={AddCompany} />
            <Route path="/analyze-data" component={AnalyzeData} />
            <Route path="/view-graphs" component={ViewGraphs} />
            <Route path="/fetch-data" component={FetchData} />
            <Route path="/settings" component={Settings} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;



/*
import logosolon from './logosolon.jpeg';
import './App.css';
import React from 'react';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logosolon} className="App-logo" alt="logo" />
        <p>
          A satisfação dos nossos clientes é a nossa prioridade.
        </p>

        <code><a href="https://www.solon-tech.com" target="_blank" rel="noopener noreferrer">Solon-Tech</a></code>
        <Dashboard />
      </header>

    </div>
  );
}
*/
