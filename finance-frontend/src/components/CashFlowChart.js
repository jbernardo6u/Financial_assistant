import React from "react";
import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

// Registrando os componentes necessários do Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const CashFlowChart = ({ years, operatingCashFlow, capitalExpenditures, netIncome }) => {
  // Dados do gráfico
  const chartData = {
    labels: years,
    datasets: [
      {
        label: 'Operating Cash Flow',
        data: operatingCashFlow,
        borderColor: "rgba(75,192,192,1)",
        backgroundColor: "rgba(75,192,192,0.2)",
        fill: true,
      },
      {
        label: 'Capital Expenditures',
        data: capitalExpenditures,
        borderColor: "rgba(255,99,132,1)",
        backgroundColor: "rgba(255,99,132,0.2)",
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
      <h3>Cash Flow Analysis (Graphical View)</h3>
      <Line data={chartData} />
    </div>
  );
};

export default CashFlowChart;
