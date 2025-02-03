import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import AddCompany from './pages/AddCompany';
import FetchData from './pages/FetchData';
import AnalyzeData from './pages/AnalyzeData';
import ViewGraphs from './pages/ViewGraphs';
import Settings from './pages/Settings';

function AppRoutes() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/add-company" element={<AddCompany />} />
        <Route path="/fetch-data" element={<FetchData />} />
        <Route path="/analyze-data" element={<AnalyzeData />} />
        <Route path="/view-graphs" element={<ViewGraphs />} />
        <Route path="/settings" component={Settings} />
      </Routes>
    </Router>
  );
}

export default AppRoutes;
