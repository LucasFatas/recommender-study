import React, { useEffect } from "react";

import { useNavigate } from 'react-router-dom';


//TODO use port and url in json file

export const IntroductionPage = (props) => {
  

  const {
    type,
    intro,
    nextpage
  } = props;



  const navigate = useNavigate();

  useEffect(() => {
    const url = sessionStorage.getItem("currentUrl")
    if(sessionStorage.getItem("userID") === null){
      console.log("you have no Id, you are redirected to the consent page")
      sessionStorage.setItem("currentUrl", "/consentPage")
      navigate("/consentPage")
    } 
    else if(url === "/introduction") {
      console.log("This is the first questionnaire")
      sessionStorage.setItem("currentUrl", "/introduction/" + type)
    }
    else if(url.includes("introduction")){
      console.log("you are in" + url)

    }
    else{
      console.log("you are redirected to", url)
      navigate(sessionStorage.getItem("currentUrl"))

    }

  }, []);

  const handleNext = () => {
    //the navigated page is possibly going to change in the future 
    sessionStorage.setItem("currentUrl", nextpage)
    navigate(nextpage)
  }
  const buttonStyleActive = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full";

 

  return (
    <div className='flex flex-col items-center justify-between h-screen w-screen py-28'>
    <h1 className="text-2xl py-5"> {intro.title} </h1>
    <div className="w-1/2 h-3/4 overflow-y-scroll">
      <p>{intro.introduction}</p>    
    </div>
    <div className="flex items-center justify-center w-fit mb-5 space-x-7 py-10">
      <button className={buttonStyleActive} onClick={handleNext} >
        <div className='grid place-items-center '>
          <span className="text-white"> next </span>
        </div>
      </button> 
    </div>
  </div>
  )
}