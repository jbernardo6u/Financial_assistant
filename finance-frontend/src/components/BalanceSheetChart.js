import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

// Registrando os componentes necessários do Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const BalanceSheetChart = ({ years, totalAssets, totalLiabilities, totalShareholderEquity }) => {
  // Dados do gráfico
  const chartData = {
    labels: years,
    datasets: [
      {
        label: 'Total Assets',
        data: totalAssets,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        fill: true,
      },
      {
        label: 'Total Liabilities',
        data: totalLiabilities,
        borderColor: "rgba(255,99,132,1)",
        backgroundColor: "rgba(255,99,132,0.2)",
        fill: true,
      },
      {
        label: 'Total Shareholder Equity',
        data: totalShareholderEquity,
        borderColor: "rgba(153,102,255,1)",
        backgroundColor: "rgba(153,102,255,0.2)",
        fill: true,
      }
    ]
  };

  return (
    <div>
      <h3>Balance Sheet Analysis (Graphical View)</h3>
      <Line data={chartData} />
    </div>
  );
};

export default BalanceSheetChart;
