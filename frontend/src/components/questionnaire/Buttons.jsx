import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { sendAnswer } from '../../API/Questionnaire';


const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
}



export const Buttons = ({ prevPage, showSubmit, nextPage, answered, answers, onNext }) => {

  const navigate = useNavigate();

  const handleSubmit = () => {
    sendAnswer(answers);
    //for the moment, the participant is direcly redirected tp the recommender, 
    // Later on, he/she will be redirected first to the result and loading page 
    navigate('/recommender');
  }

  const setStyleAndDisabled = (pageCondition, answerCondition) => {
    const { active, disabled, inactive } = buttonStyles;
    return { 
      className : pageCondition && answerCondition ? active : (pageCondition ? inactive : disabled),
      disabled : pageCondition && answerCondition === false ? true : false
    }
  }
  
  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      <Link to={ `/questionnaire/page${ prevPage }`} className={ prevPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(prevPage, true)}>
          Previous
        </button> 
      </Link>
      
      <button {...setStyleAndDisabled(showSubmit, answered)} onClick={handleSubmit}>
        Submit
      </button>

      <Link to={ `/questionnaire/page${ nextPage }` } className={ nextPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(nextPage, answered)} onClick={ onNext }>
          Next
        </button>
      </Link>
    </div>
  );
}   