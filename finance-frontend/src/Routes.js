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
            <Route exact path="/" element={<Home />} />
            <Route path="/add-company" element={<AddCompany />} />
            <Route path="/analyze-data" element={<AnalyzeData />} />
            <Route exact path="/dashboard" element={<Dashboard />} />
            <Route path="/view-graphs" element={<ViewGraphs />} />
            <Route path="/market-news" element={<MarketNews />} />
            <Route path="/fetch-data" element={<FetchData />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default AppRoutes;
