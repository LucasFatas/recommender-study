import React from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend, } from 'chart.js'; 
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const labels = ['Conformity', 'Tradition', 'Benevolence', 'Universalism', 'Self-direction', 'Stimulation', 'Hedonism', 'Achievement', 'Power', 'Security'];

const labelsFontSize = 15;

const options = {
  responsive: true,
  maintainAspectRatio: true,
  aspectRatio: 1.5,
  scales: {
    r : {
      pointLabels: {
        font: {
          size: labelsFontSize
        }
      },
    },
  },
  plugins: {
    legend: { display: false },
    title: {
      display: true,
      text: 'PVQ Test Results',
      font: { size: 16 }
    },
  },
};

export const BarChart = (props) => {

  const { result } = props;

  /*Libraries documentation : 
    - https://react-chartjs-2.js.org/
    - https://www.chartjs.org/docs/latest/
  */
  
  const data = {
    labels,
    datasets: [{
      barThickness: 30,
      data : result,
      backgroundColor: 'rgba(75, 136, 162, 0.5)'
    }]
  };

  return <Bar options={options} data={data}/>
}