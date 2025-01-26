import React from "react";

function OverviewReport({ data }) {
  if (!data) return null;

  // Função para formatar os números
  const formatNumber = (num) => {
    return num ? new Intl.NumberFormat('en-US').format(num) : 'N/A';
  };

  return (
    <div>
      <h3>{data.Name} ({data.Symbol}) Overview</h3>

      <p><strong>Description:</strong> {data.Description}</p>
      <p><strong>Industry:</strong> {data.Industry}</p>
      <p><strong>Sector:</strong> {data.Sector}</p>
      <p><strong>Country:</strong> {data.Country}</p>
      <p><strong>Exchange:</strong> {data.Exchange}</p>
      <p><strong>Market Capitalization:</strong> ${formatNumber(data.MarketCapitalization)}</p>
      <p><strong>Fiscal Year End:</strong> {data.FiscalYearEnd}</p>
      <p><strong>Latest Quarter:</strong> {data.LatestQuarter}</p>

      <h4>Financial Indicators</h4>
      <ul>
        <li><strong>EBITDA:</strong> ${formatNumber(data.EBITDA)}</li>
        <li><strong>P/E Ratio:</strong> {formatNumber(data.PERatio)}</li>
        <li><strong>PEG Ratio:</strong> {formatNumber(data.PEGRatio)}</li>
        <li><strong>Book Value:</strong> ${formatNumber(data.BookValue)}</li>
        <li><strong>Dividend Per Share:</strong> ${formatNumber(data.DividendPerShare)}</li>
        <li><strong>Dividend Yield:</strong> {data.DividendYield * 100}%</li>
        <li><strong>EPS (Earnings Per Share):</strong> ${formatNumber(data.EPS)}</li>
        <li><strong>Operating Margin:</strong> {data.OperatingMarginTTM * 100}%</li>
        <li><strong>Profit Margin:</strong> {data.ProfitMargin * 100}%</li>
        <li><strong>Return on Assets:</strong> {data.ReturnOnAssetsTTM * 100}%</li>
        <li><strong>Return on Equity:</strong> {data.ReturnOnEquityTTM * 100}%</li>
      </ul>

      <h4>Growth & Valuation</h4>
      <ul>
        <li><strong>Quarterly Earnings Growth (YoY):</strong> {data.QuarterlyEarningsGrowthYOY * 100}%</li>
        <li><strong>Quarterly Revenue Growth (YoY):</strong> {data.QuarterlyRevenueGrowthYOY * 100}%</li>
        <li><strong>Price-to-Book Ratio:</strong> {formatNumber(data.PriceToBookRatio)}</li>
        <li><strong>Price-to-Sales Ratio (TTM):</strong> {formatNumber(data.PriceToSalesRatioTTM)}</li>
      </ul>

      <h4>Stock Performance</h4>
      <ul>
        <li><strong>52 Week High:</strong> ${formatNumber(data["52WeekHigh"])}</li>
        <li><strong>52 Week Low:</strong> ${formatNumber(data["52WeekLow"])}</li>
        <li><strong>50-Day Moving Average:</strong> ${formatNumber(data["50DayMovingAverage"])}</li>
        <li><strong>200-Day Moving Average:</strong> ${formatNumber(data["200DayMovingAverage"])}</li>
      </ul>
    </div>
  );
}

export default OverviewReport;
