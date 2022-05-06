import React from 'react';
import { Link } from 'react-router-dom';

const buttonStyle = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ";
const buttonStyleDisabled = " select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full ";
const buttonStyleOpaque = "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full ";


export const Buttons = (props) => {

  const setStyleAndDisabled = (pageCondition, answerCondition) => {
    return { 
      className : pageCondition && answerCondition ? buttonStyle : (pageCondition ? buttonStyleOpaque : buttonStyleDisabled),
      disabled : pageCondition && answerCondition === false ? true : false
    }
  }
  
  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      <Link to={ `/page${props.prevPage }`} className={props.prevPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(props.prevPage, true)}>
          Previous
        </button> 
      </Link>
      
      <button {...setStyleAndDisabled(props.showSubmit, props.answered, buttonStyleOpaque)}>
        Submit
      </button>

      <Link to={ `/page${props.nextPage }` } className={props.nextPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(props.nextPage, props.answered)} onClick={props.onNext}>
          Next
        </button>
      </Link>
    </div>
  );
}