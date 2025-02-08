import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Sidebar from './layouts/Sidebar';
import Home from './pages/Home';
import AddCompany from './pages/AddCompany';
import DashboardPage from './pages/DashboardPage';
import AnalyzeData from './pages/AnalyzeData';
import ViewGraphs from './pages/ViewGraphs';
import MarketNews from './pages/MarketNews';
import FetchData from './pages/FetchData';
import Settings from './pages/Settings';
import ProtectedRoute from './components/ProtectedRoute';
import Signup from './pages/auth/Signup';
import Login from './pages/auth/Login';

function AppRoutes() {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route exact path="/dashboard" element={<DashboardPage />} />
            <Route path="/view-graphs" element={<ViewGraphs />} />
            <Route path="/market-news" element={<MarketNews />} />

            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />



            <Route path="/fetch-data" element={<ProtectedRoute element={<FetchData />} />} />
            <Route path="/add-company" element={<ProtectedRoute element={<AddCompany />} />} />
            <Route path="/analyze-data" element={<ProtectedRoute element={<AnalyzeData />} />} />
            <Route path="/settings" element={<ProtectedRoute element={<Settings />} />} />
            {/* Page 404 */}
            <Route path="*" element={<h1>Page no found</h1>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default AppRoutes;
