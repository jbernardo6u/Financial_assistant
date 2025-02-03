import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="container">
        <div className="logo">Solon Tech</div>
        <nav>
          <a href="/">Accueil</a>
          <a href="/add-company">Ajouter Entreprise</a>
          <a href="/fetch-data">Récupérer Données</a>
          <a href="/view-graphs">Graphiques</a>
        </nav>
      </div>
    </header>
  );
}

export default Header;
