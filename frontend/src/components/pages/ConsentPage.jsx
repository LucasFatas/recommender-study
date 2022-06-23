import React, { useEffect } from "react";
import { useState } from "react";

import { useLocation, useNavigate } from 'react-router-dom';
import { constentPageSecurity } from "../../controller/pathSecurityController";

const buttonDefault = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-full text-2xl";
const buttonInactive = "select-none bg-blue-300 text-white font-bold py-2 px-5 rounded-full text-2xl";



export const ConsentPage = () => {

  
  const navigate = useNavigate();


  if(sessionStorage.getItem("currentUrl") === null){
    sessionStorage.setItem("currentUrl", "/consentPage")
  }

  useEffect(() => {
    constentPageSecurity(navigate)
  }, []);
    
  const [checked, setChecked] = useState(false);


  const handleNext = () => {
    sessionStorage.setItem("currentUrl", "/websiteIntroduction");
    navigate('/websiteIntroduction')

  }

  const buttonStyles = {
    active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
    inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
  }

 

  return (
    <div className='flex flex-col items-center justify-center h-screen w-screen'>
      <div className="w-1/2 h-1/2 overflow-y-scroll">
        <p>
          You are being invited to participate in a research study conducted by Sandy Manolios from the TUDelft.
          The purpose of this research study is to compare different music recommendation approaches
          based on who people are. It will take you approximately 45 minutes to complete. We will be asking
          you to answer two surveys designed to know you better as a personn. We will also ask you to login
          into Spotify to retrieve your favorite songs. If you are a part of the longer condition, you will then be
          presented 3 lists of 5 personalized recommendations and asked to provide feedback through 6
          multiple choice questions. You will also have the option to give additional comments.
          This data will be used to provide the recommendation and compare the different approaches. The
          study is aimed to be published, along with a dataset with participants’ opinion of the
          recommendation lists. A second dataset containing the scores to the two surveys and the tops
          songs will also be published for further research purposes.
          As with any online activity the risk of a breach is always possible. To the best of our ability your
          answers in this study will remain confidential. We will minimize any risks by completely
          annonymizing the datasets. Demographic information will be reported in an aggregated way to
          show how representative our participants are of the overall population. The feedback dataset will
          only contain participants’ answers to the 6 feedback multiple choice questions about each list, as
          well as random users’ ID (not your Prolific IDs). The additional comments will be excluded, though
          they may be quoted in the paper reporting the study. To reinforce annonymization, the second
          dataset will contain different random user IDs so that your answers cannot be linked to the same
          person.
          Your participation in this study is entirely voluntary and you can withdraw at any time. Note though
          that we can only use full results in our study and therefore, will only compensate participants who
          finish the experiment by answering all of the mandatory questions.
          For more information about this research and how you data will be handeled, or for any request
          regarding this study and your data, you can contact Sandy Manolios at s.manolios@tudelft.nl
          By checking the checkbox below and going through the next page, you recognize having read and agreed to all of the above.
        </p>
      </div>
      <div className="my-10">
        <label className="inline-flex items-center">
          <input type="checkbox" className="scale-150 mx-3 w-4 h-4 border-0 focus:ring-0" checked={checked} onClick={() => setChecked(!checked)} />
          <span className="ml-2 text-lg">I accept the terms and agreements.</span>
        </label>
      </div>
      <button className={checked ? buttonDefault : buttonInactive} disabled={!checked} onClick={handleNext} >
        Next
      </button> 
    </div>
  )
}