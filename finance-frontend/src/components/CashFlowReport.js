import React from "react";

function CashFlowReport({ data }) {
  if (!data || data.length === 0) return null;

  // Função para formatar números com vírgulas para melhor legibilidade
  const formatNumber = (number) => {
    return number ? Number(number).toLocaleString() : 'N/A';
  };

  return (
    <div>
      <h3>Cash Flow</h3>

      {data.map((yearData, index) => (
        <div key={index}>
          <h4>Fiscal Year Ending: {yearData.fiscalDateEnding}</h4>
          <h5>Reported Currency: {yearData.reportedCurrency}</h5>

          <h6>Operating Activities</h6>
          <ul>
            <li><strong>Operating Cash Flow:</strong> ${formatNumber(yearData.operatingCashflow)}</li>
            <li><strong>Payments for Operating Activities:</strong> ${formatNumber(yearData.paymentsForOperatingActivities)}</li>
            <li><strong>Proceeds from Operating Activities:</strong> {yearData.proceedsFromOperatingActivities || 'N/A'}</li>
            <li><strong>Change in Operating Liabilities:</strong> ${formatNumber(yearData.changeInOperatingLiabilities)}</li>
            <li><strong>Change in Operating Assets:</strong> ${formatNumber(yearData.changeInOperatingAssets)}</li>
            <li><strong>Depreciation, Depletion, and Amortization:</strong> ${formatNumber(yearData.depreciationDepletionAndAmortization)}</li>
          </ul>

          <h6>Investment Activities</h6>
          <ul>
            <li><strong>Capital Expenditures:</strong> ${formatNumber(yearData.capitalExpenditures)}</li>
            <li><strong>Change in Receivables:</strong> ${formatNumber(yearData.changeInReceivables)}</li>
            <li><strong>Change in Inventory:</strong> ${formatNumber(yearData.changeInInventory)}</li>
            <li><strong>Cash Flow from Investment:</strong> ${formatNumber(yearData.cashflowFromInvestment)}</li>
          </ul>

          <h6>Financing Activities</h6>
          <ul>
            <li><strong>Cash Flow from Financing:</strong> ${formatNumber(yearData.cashflowFromFinancing)}</li>
            <li><strong>Proceeds from Repayments of Short-Term Debt:</strong> ${formatNumber(yearData.proceedsFromRepaymentsOfShortTermDebt)}</li>
            <li><strong>Dividend Payout:</strong> ${formatNumber(yearData.dividendPayout)}</li>
            <li><strong>Dividend Payout Common Stock:</strong> ${formatNumber(yearData.dividendPayoutCommonStock)}</li>
            <li><strong>Proceeds from Issuance of Long-Term Debt and Capital Securities:</strong> ${formatNumber(yearData.proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet)}</li>
          </ul>

          <h6>Other Activities</h6>
          <ul>
            <li><strong>Net Income:</strong> ${formatNumber(yearData.netIncome)}</li>
            <li><strong>Change in Cash and Cash Equivalents:</strong> {yearData.changeInCashAndCashEquivalents || 'N/A'}</li>
            <li><strong>Change in Exchange Rate:</strong> {yearData.changeInExchangeRate || 'N/A'}</li>
          </ul>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default CashFlowReport;
