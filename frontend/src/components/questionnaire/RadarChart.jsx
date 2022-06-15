import React from "react";
import {  Chart as ChartJS, RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend, } from 'chart.js';
import { Radar } from "react-chartjs-2";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

const labels = ['Honesty', 'Emotionality', 'Extraversion', 'Agreeableness', 'Conscientiousness', 'Openness to Experience'];
const labelsFontSize = 15;

const options = {
  responsive: true,
  maintainAspectRatio: true,
  aspectRatio: 1.5,
  scales: {
    r : {
      beginAtZero : true,
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
      text: 'HEXACO Test Results',
      font: { size: 16 }
    },
  },
};

export const RadarChart = (props) => {

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
      backgroundColor: 'rgba(187, 10, 33, 0.5)'
    }]
  };

  return <Radar options={options} data={data}/>
}