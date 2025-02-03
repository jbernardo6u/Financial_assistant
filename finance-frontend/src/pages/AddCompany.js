import React, { useState } from 'react';
import axios from 'axios';

function AddCompany() {
  const [name, setName] = useState('');
  const [symbol, setSymbol] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://localhost:8000/api/companies/', { name, symbol })
      .then((response) => setMessage('Entreprise ajoutée avec succès !'))
      .catch((error) =>
        setMessage('Erreur lors de l’ajout de l’entreprise : ' + error.message)
      );
  };

  return (
    <div className="container">
      <h2>Ajouter une entreprise</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Nom de l'entreprise"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Symbole boursier"
          value={symbol}
          onChange={(e) => setSymbol(e.target.value)}
          required
        />
        <button type="submit">Ajouter</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default AddCompany;
