import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css'; // Assurez-vous de créer un fichier CSS correspondant pour styliser la barre latérale.

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>Finance Assistant</h2>
      </div>
      <nav className="sidebar-nav">
        <ul>
        <li>
            <NavLink exact to="/" activeClassName="active">
              Home
            </NavLink>
          </li>
          <li>
            <NavLink to="/add-company" activeClassName="active">
              Add company
            </NavLink>
          </li>
          <li>
            <NavLink to="/analyze-data" activeClassName="active">
              Analyze sociaties
            </NavLink>
          </li>
          <li>
            <NavLink exact to="/dashboard" activeClassName="active">
              Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink to="/view-graphs" activeClassName="active">
              See tendencies
            </NavLink>
          </li>
          <li>
            <NavLink to="/market-news" activeClassName="active">
              Market news
            </NavLink>
          </li>
          <li>
            <NavLink to="/settings" activeClassName="active">
              Settings
            </NavLink>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
