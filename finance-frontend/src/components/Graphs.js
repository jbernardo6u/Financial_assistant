import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Chart } from 'chart.js/auto';

function Graphs() {
  const [indicators, setIndicators] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/indicators/')
      .then(response => setIndicators(response.data))
      .catch(error => console.error(error));
  }, []);

  useEffect(() => {
    if (indicators.length) {
      const ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: indicators.map(indicator => indicator.year),
          datasets: [
            {
              label: 'Rentabilité (ROE)',
              data: indicators.map(indicator => indicator.roe),
              borderColor: 'blue',
            },
            {
              label: 'Croissance des Revenus',
              data: indicators.map(indicator => indicator.revenue_growth),
              borderColor: 'green',
            },
          ],
        },
      });
    }
  }, [indicators]);

  return (
    <div>
      <h1>Graphiques des Indicateurs</h1>
      <canvas id="myChart"></canvas>
    </div>
  );
}

export default Graphs;
