import React, { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const buttonDefault = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-full text-2xl";
const buttonInactive = "select-none bg-blue-300 text-white font-bold py-2 px-5 rounded-full text-2xl";
const buttonDisabled = "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-5 rounded-full text-2xl";

export const Buttons = (props) => {

  console.log(typeof(buttonInactive));

  const [showWarning, setShowWarning] = useState(false);

  useEffect(() => {
    //Because of the functions onMouseEnter/Leave, sometimes the warning error gets stuck 
    //This function hides it if it's still visible after 2 seconds.
    if (showWarning) {
      const timeout = setTimeout(() => setShowWarning(false), 2000);
      return () => clearTimeout(timeout);
    }
  }, [showWarning])
  
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

    sessionStorage.setItem("currentUrl", pathOnSubmit)
    navigate(pathOnSubmit);
  }

  const setStyleAndDisabled = (pageCondition, answerCondition) => {
    return { 
      className : pageCondition && answerCondition ? buttonDefault : (pageCondition ? buttonInactive : buttonDisabled),
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

      <Link 
        to={ nextPage && answered ? `${currentPath}/page${ nextPage }` : '#' }  
        onMouseEnter={() => {
          if (!(nextPage && answered))
            setShowWarning(true)
        }}
        onMouseLeave={() => setShowWarning(false)}
      >
        <div>
          <button {...setStyleAndDisabled(nextPage, answered)} onClick={ onNext }>
            Next
          </button>
        </div>
      </Link>
      {
        showWarning 
        ?
        <div className={'absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-1/4 text-center bg-neutral-100 rounded-lg text-xl border-solid border-2 border-rose-500 p-2'}>
          <h3 className='text-rose-700'>Please fill out all questions before proceeding to next the page</h3>
        </div>
        : ""
      } 
    </div>
  );
}   