import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
  const [companies, setCompanies] = useState([]);
  const [selectedCompany, setSelectedCompany] = useState('');
  const [year, setYear] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/companies/')
      .then(response => setCompanies(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleFetchData = () => {
    axios.post('http://localhost:8000/api/fetch_financial_data/', {
      company_id: selectedCompany,
      num_of_exercice_year: year,
    })
    .then(response => setMessage(response.data.message))
    .catch(error => setMessage(error.response ? error.response.data.error : "Error fetching data"));
  };

  const handleCalculateIndicators = () => {
    axios.post('http://localhost:8000/api/calculate_indicators/', {
      company_id: selectedCompany,
    })
    .then(response => setMessage(response.data.message))
    .catch(error => setMessage(error.response ? error.response.data.error : "Error calculating indicators"));
  };

  const handleViewGraphs = () => {
    window.location.href = '/graphs';
  };

  const handleChatbotInteraction = () => {
    window.location.href = '/chatbot';
  };

  return (
    <div>
      <h1>Assistente Financeiro</h1>
      <select onChange={(e) => setSelectedCompany(e.target.value)}>
        <option value="">Selecionar Empresa</option>
        {companies.map((company) => (
          <option key={company.id} value={company.id}>{company.name}</option>
        ))}
      </select>
      <input type="number" placeholder="Número de anos a analisar" value={year} onChange={(e) => setYear(e.target.value)} />
      <button onClick={handleFetchData}>Récupérer Données</button>
      <button onClick={handleCalculateIndicators}>Analyser Données</button>
      <button onClick={handleViewGraphs}>Voir Graphiques</button>
      <button onClick={handleChatbotInteraction}>Chatbot</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Dashboard;
