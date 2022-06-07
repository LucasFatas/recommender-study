import React, { useState,  useEffect } from "react";
import { Link } from "react-router-dom";

import { Loading } from '../global/Loading';
import { Chart } from "./Chart";
import { getLastPage } from "../../controller/questionnaireController";

export const QuestionnaireResult = (props) => {
  
  const { currentBatch } = props;

  /*
    Personality : [3.0, 2.7, 3.7, 3.9, 2.8, 3.3],
    Values : [0.35, -0.65, 0.1, 1.18, -0.15, -1.32, -0.32, -0.15, 0.02, -0.05]
  */
  const [results, setResults] = useState(JSON.parse(sessionStorage.getItem("questionnaireResults")));

  useEffect(() => {
    if (!results)
      //setResults(JSON.parse(sessionStorage.getItem("questionnaireResults")));
      setResults({
        personality : [3.0, 2.7, 3.7, 3.9, 2.8, 3.3],
        values : [0.35, -0.65, 0.1, 1.18, -0.15, -1.32, -0.32, -0.15, 0.02, -0.05]
      })
  }, [results]);

  const lastPage = getLastPage(currentBatch);

  return (
    <>
      {results 
        ?
        <div className="flex flex-col w-screen h-screen flex justify-center items-center">
          <div className="w-1/3 h-5/6 grid grid-rows-2 grid-cols-1 gap-20 items-center justify-center">
            <Chart type="personality" result={results.personality}/>
            <Chart type="values" result={results.values}/>
          </div>
          <div className="mt-10">
            <Link to={lastPage}>
              <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ">Next</button>
            </Link> 
          </div>
        </div>
        : <Loading/> 
      }
    </>
  )
}