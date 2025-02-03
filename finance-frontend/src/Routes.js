import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './layouts/Sidebar';
import Home from './pages/Home';
import AddCompany from './pages/AddCompany';
import Dashboard from './components/Dashboard';
import AnalyzeData from './pages/AnalyzeData';
import ViewGraphs from './pages/ViewGraphs';
import MarketNews from './pages/MarketNews';
import FetchData from './pages/FetchData';
import Settings from './pages/Settings';

function AppRoutes() {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route exact path="/" component={Home} />
            <Route path="/add-company" component={AddCompany} />
            <Route path="/analyze-data" component={AnalyzeData} />
            <Route exact path="/dashboard" component={Dashboard} />
            <Route path="/view-graphs" component={ViewGraphs} />
            <Route path="/market-news" component={MarketNews} />
            <Route path="/fetch-data" component={FetchData} />
            <Route path="/settings" component={Settings} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default AppRoutes;
