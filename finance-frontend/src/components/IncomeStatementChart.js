import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

// Registrando os componentes necessários do Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const IncomeStatementChart = ({ years, totalRevenue, grossProfit, operatingIncome, netIncome }) => {
  // Dados do gráfico
  const chartData = {
    labels: years,
    datasets: [
      {
        label: 'Total Revenue',
        data: totalRevenue,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        fill: true,
      },
      {
        label: 'Gross Profit',
        data: grossProfit,
        borderColor: "rgba(54,162,235,1)",
        backgroundColor: "rgba(54,162,235,0.2)",
        fill: true,
      },
      {
        label: 'Operating Income',
        data: operatingIncome,
        borderColor: "rgba(255,159,64,1)",
        backgroundColor: "rgba(255,159,64,0.2)",
        fill: true,
      },
      {
        label: 'Net Income',
        data: netIncome,
        borderColor: "rgba(153,102,255,1)",
        backgroundColor: "rgba(153,102,255,0.2)",
        fill: true,
      }
    ]
  };

  return (
    <div>
      <h3>Income Statement Analysis (Graphical View)</h3>
      <Line data={chartData} />
    </div>
  );
};

export default IncomeStatementChart;
