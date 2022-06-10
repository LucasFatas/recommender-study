import React, { useState,  useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

import { BarChart } from "./BarChart";
import { RadarChart } from "./RadarChart";
import { Loading } from '../global/Loading';

import { loadResultsIfStored } from "../../controller/questionnaireController";
import { getBatch } from "../../API/Dashboard";
import { getLastPage } from "../../controller/questionnaireController";
import { sendAnswer } from '../../API/Questionnaire';

export const QuestionnaireResult = () => {

  const navigate = useNavigate();

  useEffect(() => {
    if(sessionStorage.getItem("currentUrl") !== "/questionnaire/results"){
      console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
      navigate(sessionStorage.getItem("currentUrl"))
    }
    else
    {
      console.log("you are in", sessionStorage.getItem("currentUrl"))
    }

  }, []);

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
              <RadarChart result={results.personality}/>
              <p className="mt-20">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae quia ipsa, saepe illum commodi, laudantium nihil magni quasi quas asperiores totam, dignissimos odio corrupti obcaecati. Exercitationem aliquam rerum amet quod eveniet, nobis reprehenderit numquam voluptatum maiores sequi dolores cupiditate consequuntur praesentium nihil omnis! Aut nemo nostrum aliquid, autem commodi corporis?</p>
            </div>
            <div className="w-2/5 ">
              <BarChart  result={results.values}/>
              <p className="mt-20">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae quia ipsa, saepe illum commodi, laudantium nihil magni quasi quas asperiores totam, dignissimos odio corrupti obcaecati. Exercitationem aliquam rerum amet quod eveniet, nobis reprehenderit numquam voluptatum maiores sequi dolores cupiditate consequuntur praesentium nihil omnis! Aut nemo nostrum aliquid, autem commodi corporis?</p>
            </div>
          </div>
          <div className="mt-10">
            <Link to={lastPage}>
              <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full " onClick={() => sessionStorage.setItem("currentUrl", lastPage)}>Next</button>
            </Link> 
          </div>
        </div>
        : <Loading/> 
      }
    </>
  )
}