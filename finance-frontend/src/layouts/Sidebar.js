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
              Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink to="/add-company" activeClassName="active">
              Ajouter une Entreprise
            </NavLink>
          </li>
          <li>
            <NavLink to="/analyze-data" activeClassName="active">
              Analyser les Données
            </NavLink>
          </li>
          <li>
            <NavLink to="/view-graphs" activeClassName="active">
              Voir les Graphiques
            </NavLink>
          </li>
          <li>
            <NavLink to="/settings" activeClassName="active">
              Paramètres
            </NavLink>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Sidebar;
