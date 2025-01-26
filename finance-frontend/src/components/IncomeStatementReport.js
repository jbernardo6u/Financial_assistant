import React from "react";

function IncomeStatementReport({ data }) {
  if (!data || data.length === 0) return null;

  // Função para formatar números com vírgulas para melhor legibilidade
  const formatNumber = (number) => {
    return number ? Number(number).toLocaleString() : 'N/A';
  };

  return (
    <div>
      <h3>Income Statement</h3>

      {data.map((yearData, index) => (
        <div key={index}>
          <h4>Fiscal Year Ending: {yearData.fiscalDateEnding}</h4>
          <h5>Reported Currency: {yearData.reportedCurrency}</h5>

          <h6>Revenue & Profit</h6>
          <ul>
            <li><strong>Total Revenue:</strong> ${formatNumber(yearData.totalRevenue)}</li>
            <li><strong>Gross Profit:</strong> ${formatNumber(yearData.grossProfit)}</li>
            <li><strong>Operating Income:</strong> ${formatNumber(yearData.operatingIncome)}</li>
            <li><strong>Net Income:</strong> ${formatNumber(yearData.netIncome)}</li>
            <li><strong>EBIT:</strong> ${formatNumber(yearData.ebit)}</li>
            <li><strong>EBITDA:</strong> ${formatNumber(yearData.ebitda)}</li>
          </ul>

          <h6>Expenses</h6>
          <ul>
            <li><strong>Cost of Revenue:</strong> ${formatNumber(yearData.costOfRevenue)}</li>
            <li><strong>Selling, General and Administrative Expenses:</strong> ${formatNumber(yearData.sellingGeneralAndAdministrative)}</li>
            <li><strong>Research and Development Expenses:</strong> ${formatNumber(yearData.researchAndDevelopment)}</li>
            <li><strong>Operating Expenses:</strong> ${formatNumber(yearData.operatingExpenses)}</li>
          </ul>

          <h6>Other Financial Information</h6>
          <ul>
            <li><strong>Income Before Tax:</strong> ${formatNumber(yearData.incomeBeforeTax)}</li>
            <li><strong>Income Tax Expense:</strong> ${formatNumber(yearData.incomeTaxExpense)}</li>
            <li><strong>Interest Expense:</strong> ${formatNumber(yearData.interestExpense)}</li>
            <li><strong>Net Income From Continuing Operations:</strong> ${formatNumber(yearData.netIncomeFromContinuingOperations)}</li>
            <li><strong>Comprehensive Income (Net of Tax):</strong> ${formatNumber(yearData.comprehensiveIncomeNetOfTax)}</li>
          </ul>

          <h6>Depreciation & Amortization</h6>
          <ul>
            <li><strong>Depreciation:</strong> ${formatNumber(yearData.depreciation)}</li>
            <li><strong>Depreciation and Amortization:</strong> ${formatNumber(yearData.depreciationAndAmortization)}</li>
          </ul>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default IncomeStatementReport;
