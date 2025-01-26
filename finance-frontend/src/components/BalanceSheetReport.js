import React from "react";

function BalanceSheetReport({ data }) {
  if (!data || data.length === 0) return null;

  // Função para formatar números com vírgulas para melhor legibilidade
  const formatNumber = (number) => {
    return number ? Number(number).toLocaleString() : 'N/A';
  };

  return (
    <div>
      <h3>Balance Sheet</h3>

      {data.map((yearData, index) => (
        <div key={index}>
          <h4>Fiscal Year Ending: {yearData.fiscalDateEnding}</h4>
          <h5>Reported Currency: {yearData.reportedCurrency}</h5>

          <h6>Assets</h6>
          <ul>
            <li><strong>Total Assets:</strong> ${formatNumber(yearData.totalAssets)}</li>
            <li><strong>Total Current Assets:</strong> ${formatNumber(yearData.totalCurrentAssets)}</li>
            <li><strong>Cash and Cash Equivalents:</strong> ${formatNumber(yearData.cashAndCashEquivalentsAtCarryingValue)}</li>
            <li><strong>Inventory:</strong> ${formatNumber(yearData.inventory)}</li>
            <li><strong>Current Net Receivables:</strong> ${formatNumber(yearData.currentNetReceivables)}</li>
            <li><strong>Total Non-Current Assets:</strong> ${formatNumber(yearData.totalNonCurrentAssets)}</li>
            <li><strong>Property, Plant and Equipment:</strong> ${formatNumber(yearData.propertyPlantEquipment)}</li>
            <li><strong>Intangible Assets:</strong> ${formatNumber(yearData.intangibleAssets)}</li>
            <li><strong>Goodwill:</strong> ${formatNumber(yearData.goodwill)}</li>
          </ul>

          <h6>Liabilities</h6>
          <ul>
            <li><strong>Total Liabilities:</strong> ${formatNumber(yearData.totalLiabilities)}</li>
            <li><strong>Total Current Liabilities:</strong> ${formatNumber(yearData.totalCurrentLiabilities)}</li>
            <li><strong>Current Accounts Payable:</strong> ${formatNumber(yearData.currentAccountsPayable)}</li>
            <li><strong>Deferred Revenue:</strong> ${formatNumber(yearData.deferredRevenue)}</li>
            <li><strong>Current Debt:</strong> ${formatNumber(yearData.currentDebt)}</li>
            <li><strong>Total Non-Current Liabilities:</strong> ${formatNumber(yearData.totalNonCurrentLiabilities)}</li>
            <li><strong>Long-Term Debt:</strong> ${formatNumber(yearData.longTermDebt)}</li>
          </ul>

          <h6>Equity</h6>
          <ul>
            <li><strong>Total Shareholder Equity:</strong> ${formatNumber(yearData.totalShareholderEquity)}</li>
            <li><strong>Treasury Stock:</strong> ${formatNumber(yearData.treasuryStock)}</li>
            <li><strong>Retained Earnings:</strong> ${formatNumber(yearData.retainedEarnings)}</li>
            <li><strong>Common Stock:</strong> ${formatNumber(yearData.commonStock)}</li>
            <li><strong>Common Stock Shares Outstanding:</strong> {formatNumber(yearData.commonStockSharesOutstanding)}</li>
          </ul>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default BalanceSheetReport;
