import React from 'react';
import logosolon from '../logosolon.jpeg';
import '../App.css';


function Home() {
  return (
    <div className="home container">
    <header className="App-header">
        <img src={logosolon} className="App-logo" alt="logo" />
        <p>
          A satisfação dos nossos clientes é a nossa prioridade.
        </p>

        <code><a href="https://www.solon-tech.com" target="_blank" rel="noopener noreferrer">Solon-Tech</a></code>
      </header>
      <h1>Bienvenue chez Solon Tech</h1>
      <p>
        Votre assistant financier virtuel pour simplifier l'analyse et la
        gestion des investissements. Sélectionnez une option ci-dessus pour
        commencer.
      </p>
    </div>
  );
}


export default Home;
