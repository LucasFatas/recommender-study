import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full pointer-events-none ",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full pointer-events-none "
}

export const Buttons = (props) => {

  const { 
    prevPage, //boolean condition to decide whether to show previous button
    showSubmit, //boolean condition to decide whether to show submit button
    nextPage, //boolean condition to decide whether to show next button
    answered,  //boolean condition to decide whether to activate next button
    onNext, //function to execute everytime next button is pressed
    data, //data object, parameters are specified right below
    pathOnSubmit, //path to route after submit button is pressed
    submitFunction, //function to execute on submit
    currentPath, //current path of the page
    submitResults //boolean condition to decide whether to execute submit function
  } = props;

  //data recommender : ratings, comment,  playlistName
  //data questionnaire : answers

  const navigate = useNavigate();

  const handleSubmit = () => {
    if (submitResults &&submitFunction)
      submitFunction(data, navigate);
      
    navigate(pathOnSubmit);
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

      <Link to={ `${currentPath}/page${ prevPage }`} className={ prevPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(prevPage, true)}>
          Previous
        </button> 
      </Link>
      
      <button {...setStyleAndDisabled(showSubmit, answered)} onClick={handleSubmit}>
        Submit
      </button>

      <Link to={ `${currentPath}/page${ nextPage }` } className={ nextPage && answered ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(nextPage, answered)} onClick={ onNext }>
          Next
        </button>
      </Link>

    </div>
  );
}   