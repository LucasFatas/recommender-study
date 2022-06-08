import React, { useState,  useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

import { Chart } from "./Chart";
import { Loading } from '../global/Loading';

import { loadResultsIfStored } from "../../controller/questionnaireController";
import { getBatch } from "../../API/Dashboard";
import { getLastPage } from "../../controller/questionnaireController";
import { sendAnswer } from '../../API/Questionnaire';

export const QuestionnaireResult = () => {

  const navigate = useNavigate();

  const [currentBatch, setCurrentBatch] = useState("");
  getBatch(setCurrentBatch, "batch")
  const lastPage = getLastPage(currentBatch === "1" ? "questionnaire" : "recommender");

  const [loading, setLoading] = useState(true);
  const [results, setResults] = useState(loadResultsIfStored(sessionStorage.getItem("questionnaireResults")));

  useEffect(() => {
    const flag = JSON.parse(sessionStorage.getItem("answerSent"));
    if (!flag)
      sendAnswer(navigate, setLoading, setResults);
  }, [loading]);

  return (
    <>
      {results 
        ?
        <div className="w-screen h-screen flex flex-col items-center justify-center">
          <div className="w-full h-5/6 flex items-center justify-center">
            <div className="w-2/5">
              <Chart type="personality" result={results.personality}/>
            </div>
            <div className="w-2/5 ">
              <Chart type="values" result={results.values}/>
            </div>
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