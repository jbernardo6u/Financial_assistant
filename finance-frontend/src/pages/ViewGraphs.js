import React from 'react';
import { Line } from 'react-chartjs-2';  // Import the Line chart component from react-chartjs-2

function ViewGraphs() {
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
    <div className="view-graphs container">
      <h2>Graphiques Financiers</h2>
      <Line data={data} />
    </div>
  );
}

export default ViewGraphs;

