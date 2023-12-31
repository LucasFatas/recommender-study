import React, { useEffect } from "react";

import { useNavigate } from 'react-router-dom';
import { introductionPagesSecurity } from "../../../controller/pathSecurityController";

const buttonDefault = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-full text-2xl";

export const IntroductionPage = (props) => {
  
  const {
    type,
    intro,
    nextpage
  } = props;

  const navigate = useNavigate();

  useEffect(() => {
    introductionPagesSecurity(navigate, type)
  }, []);

  const handleNext = () => {
    //the navigated page is possibly going to change in the future 
    sessionStorage.setItem("currentUrl", nextpage)
    navigate(nextpage)
  }

  return (
    <div className='flex flex-col items-center justify-center h-screen w-screen py-28'>
    <h1 className="text-2xl py-5"> {intro.title} </h1>
    <div className="w-3/5 h-auto text-xl py-32">
      <p>{intro.introduction}</p>    
    </div>
    <div className="flex items-center justify-center w-fit mb-5 space-x-7 py-10">
      <button className={buttonDefault} onClick={handleNext} >
         Next 
      </button>
    </div>
  </div>
  )
}