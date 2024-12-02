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
      year: year,
    })
    .then(response => setMessage(response.data.message))
    .catch(error => setMessage(error.response ? error.response.data.error : "Error fetching data"));
  };

  return (
    <div>
      <h1>Financial Dashboard</h1>
      <select onChange={(e) => setSelectedCompany(e.target.value)}>
        <option value="">Select Company</option>
        {companies.map((company) => (
          <option key={company.id} value={company.id}>{company.name}</option>
        ))}
      </select>
      <input type="text" placeholder="Year" value={year} onChange={(e) => setYear(e.target.value)} />
      <button onClick={handleFetchData}>Fetch Data</button>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Dashboard;
