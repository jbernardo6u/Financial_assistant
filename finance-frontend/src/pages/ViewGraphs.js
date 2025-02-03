import React from 'react';
import Chart from 'chart.js/auto';

function ViewGraphs() {
  // Mock data for demonstration purposes
  const data = {
    labels: ['2019', '2020', '2021', '2022', '2023'],
    datasets: [
      {
        label: 'Croissance du Profit',
        data: [10, 20, 30, 40, 50],
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
      },
    ],
  };

  return (
    <div className="container">
      <h2>Graphiques Financiers</h2>
      <canvas id="chart" />
      <Chart type="line" data={data} />
    </div>
  );
}

export default ViewGraphs;
