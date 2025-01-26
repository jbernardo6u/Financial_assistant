import React, { useState, useEffect } from "react";
import axios from "axios";
import OverviewReport from "./OverviewReport";
import IncomeStatementReport from "./IncomeStatementReport";
import BalanceSheetReport from "./BalanceSheetReport";
import CashFlowReport from "./CashFlowReport";

function Dashboard() {
  const [companies, setCompanies] = useState([]);
  const [newCompanyName, setNewCompanyName] = useState("");
  const [newCompanySymbol, setNewCompanySymbol] = useState("");
  const [selectedCompany, setSelectedCompany] = useState("");
  const [reportType, setReportType] = useState(""); // Default empty to force selection
  const [numYears, setNumYears] = useState(5); // Default 5 years
  const [message, setMessage] = useState("");
  const [financialData, setFinancialData] = useState(null);

  // Fetch list of companies on component mount
  useEffect(() => {
    fetchCompanies();
  }, []);

  const fetchCompanies = () => {
    axios
      .get("http://localhost:8000/api/companies/")
      .then((response) => setCompanies(response.data))
      .catch((error) => console.error("Error fetching companies:", error));
  };

  const handleAddCompany = () => {
    if (!newCompanyName || !newCompanySymbol) {
      setMessage("Please provide both company name and symbol.");
      return;
    }

    axios
      .post("http://localhost:8000/api/companies/", {
        name: newCompanyName,
        symbol: newCompanySymbol,
      })
      .then((response) => {
        setMessage(`Company ${response.data.name} added successfully!`);
        fetchCompanies(); // Refresh company list
        setNewCompanyName("");
        setNewCompanySymbol("");
      })
      .catch((error) =>
        setMessage(error.response?.data?.error || "Error adding company.")
      );
  };

  const handleFetchData = () => {
    if (!selectedCompany || !reportType || numYears < 1 || numYears > 10) {
      setMessage(
        "Please select a company, report type, and specify a valid number of years (1-10)."
      );
      return;
    }

    axios
      .post("http://localhost:8000/api/companies/fetch-financial-data/", {
        company_id: selectedCompany,
        report_type: reportType,
        num_of_exercise_years: numYears,
      })
      .then((response) => {
        setMessage(response.data.message);
        setFinancialData(response.data.data); // Store financial data
        setReportType(response.data.report_type); // Set report type to ensure correct display
      })
      .catch((error) =>
        setMessage(error.response?.data?.error || "Error fetching data.")
      );
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
        <select
          value={selectedCompany}
          onChange={(e) => setSelectedCompany(e.target.value)}
        >
          <option value="">-- Select a Company --</option>
          {companies.map((company) => (
            <option key={company.id} value={company.id}>
              {company.name} ({company.symbol})
            </option>
          ))}
        </select>

        {/* Select Report Type */}
        <select
          value={reportType}
          onChange={(e) => setReportType(e.target.value)}
        >
          <option value="">-- Select Report Type --</option>
          <option value="INCOME_STATEMENT">Income Statement</option>
          <option value="BALANCE_SHEET">Balance Sheet</option>
          <option value="CASH_FLOW">Cash Flow</option>
          <option value="OVERVIEW">Overview</option>
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

      {reportType === "OVERVIEW" && financialData && (
        <OverviewReport data={financialData} />
      )}

      {reportType === "INCOME_STATEMENT" && financialData && (
        <IncomeStatementReport data={financialData} />
      )}

      {reportType === "BALANCE_SHEET" && financialData && (
        <BalanceSheetReport data={financialData} />
      )}

      {reportType === "CASH_FLOW" && financialData && (
        <CashFlowReport data={financialData} />
      )}
    </div>
  );
}

export default Dashboard;
