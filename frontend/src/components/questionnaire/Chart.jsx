import React from "react";
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js';
import { Radar } from "react-chartjs-2";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

const labelsObj = {
  personality : [
    'Honesty', 'Emotionality', 'Extraversion', 
    'Agreeableness', 'Conscientiousness', 'Openness to Experience'
  ],
  values : [
    'Conformity', 'Tradition', 'Benevolence', 'Universalism', 
    'Self-direction', 'Stimulation', 'Hedonism', 
    'Achievement', 'Power', 'Security'
  ]
};

export const Chart = (props) => {

  const {
    result,
    type
  } = props;

  const labels = labelsObj[type];
  const capitalizedTitle = type.charAt(0).toUpperCase() + type.slice(1);

  /*Libraries documentation : 
    - https://react-chartjs-2.js.org/
    - https://www.chartjs.org/docs/latest/
  */

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 1.5,
    scales: {
      r : {
        pointLabels: {
          font: {
            size: 15
          }
        },
      },
    },
    plugins: {
      legend: { display: false },
      title: {
        display: true,
        text: capitalizedTitle,
        font: { size: 16 }
      },
    },
  };
  
  
  const data = {
    labels,
    datasets: [{
      barThickness: 30,
      data : result,
      backgroundColor: type === 'values' ? 'rgba(75, 136, 162, 0.5)' : 'rgba(187, 10, 33, 0.5)'
    }]
  };

  return <Radar options={options} data={data}/>
}