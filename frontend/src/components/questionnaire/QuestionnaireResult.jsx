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