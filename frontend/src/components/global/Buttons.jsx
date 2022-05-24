import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full pointer-events-none ",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full pointer-events-none "
}

export const Buttons = (props) => {

  const { 
    prevPage, 
    showSubmit, 
    nextPage, 
    answered,  
    onNext, 
    data, 
    pathOnSubmit, 
    submitFunction, 
    currentPath 
  } = props;

  //data recommender : ratings, comment,  playlistName
  //data questionnaire : answers

  const navigate = useNavigate();

  const handleSubmit = () => {
    submitFunction(data);
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