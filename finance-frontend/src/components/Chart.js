import React from 'react';
import { Bar } from 'react-chartjs-2';

function Chart({ data }) {
  const chartData = {
    labels: ['Gross Profit Margin', 'Net Profit Margin', 'Debt Ratio', 'Free Cash Flow'],
    datasets: [
      {
        label: 'Financial Indicators',
        data: data,
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return <Bar data={chartData} />;
}

export default Chart;
