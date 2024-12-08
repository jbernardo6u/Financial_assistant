import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
  const [companies, setCompanies] = useState([]);
  const [newCompanyName, setNewCompanyName] = useState('');
  const [newCompanySymbol, setNewCompanySymbol] = useState('');
  const [selectedCompany, setSelectedCompany] = useState('');
  const [numYears, setNumYears] = useState(5); // Default 5 years
  const [message, setMessage] = useState('');

  // Fetch list of companies on component mount
  useEffect(() => {
    fetchCompanies();
  }, []);

  const fetchCompanies = () => {
    axios.get('http://localhost:8000/api/companies/')
      .then(response => setCompanies(response.data))
      .catch(error => console.error('Error fetching companies:', error));
  };

  const handleAddCompany = () => {
    if (!newCompanyName || !newCompanySymbol) {
      setMessage("Please provide both company name and symbol.");
      return;
    }

    axios.post('http://localhost:8000/api/companies/', {
      name: newCompanyName,
      symbol: newCompanySymbol,
    })
      .then(response => {
        setMessage(`Company ${response.data.name} added successfully!`);
        fetchCompanies(); // Refresh company list
        setNewCompanyName('');
        setNewCompanySymbol('');
      })
      .catch(error => setMessage(error.response?.data?.error || 'Error adding company.'));
  };

  const handleFetchData = () => {
    if (!selectedCompany || !numYears) {
      setMessage("Please select a company and specify the number of years.");
      return;
    }

    axios.post('http://localhost:8000/api/companies/fetch-financial-data/', {
      company_id: selectedCompany,
      num_of_exercise_years: numYears,
    })
      .then(response => setMessage(response.data.message))
      .catch(error => setMessage(error.response?.data?.error || 'Error fetching data.'));
  };

  return (
    <div>
      <h1>Finance Assistant Dashboard</h1>

      {/* Add Company Form */}
      <div>
        <h2>Add New Company</h2>
        <input
          type="text"
          placeholder="Company Name"
          value={newCompanyName}
          onChange={(e) => setNewCompanyName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Company Symbol"
          value={newCompanySymbol}
          onChange={(e) => setNewCompanySymbol(e.target.value)}
        />
        <button onClick={handleAddCompany}>Add Company</button>
      </div>

      {/* Select Company and Fetch Data */}
      <div>
        <h2>Fetch Financial Data</h2>
        <select value={selectedCompany} onChange={(e) => setSelectedCompany(e.target.value)}>
          <option value="">-- Select a Company --</option>
          {companies.map(company => (
            <option key={company.id} value={company.id}>{company.name} ({company.symbol})</option>
          ))}
        </select>
        <input
          type="number"
          placeholder="Number of Years"
          value={numYears}
          onChange={(e) => setNumYears(e.target.value)}
          min="1"
          max="10"
        />
        <button onClick={handleFetchData}>Fetch Data</button>
      </div>

      {/* Status Message */}
      {message && <p>{message}</p>}
    </div>
  );
}

export default Dashboard;
