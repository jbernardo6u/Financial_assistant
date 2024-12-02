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

export default App;
