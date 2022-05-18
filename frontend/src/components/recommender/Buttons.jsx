import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { sendRatings } from "../../API/Recommender";


const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
}



export const Buttons = ({ prevPage, showSubmit, nextPage, answered, ratings, comment, onNext, playlistName }) => {

  const Playlistrated = 0 !== ratings[playlistName].playlist

  const navigate = useNavigate();

  const handleSubmit = () => {

    sendRatings({"ratings" : ratings, "comment" : comment});
		navigate('/thanks');
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
      <Link to={ `/recommender/page${ prevPage }`} className={ prevPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(prevPage, true)}>
          Previous
        </button> 
      </Link>
      
      <button {...setStyleAndDisabled(showSubmit, answered)} onClick={handleSubmit}>
        Submit
      </button>

      <Link to={ `/recommender/page${ nextPage }` } className={ nextPage ? "" : "pointer-events-none"}>
        <button {...setStyleAndDisabled(nextPage, Playlistrated)} onClick={ onNext }>
          Next
        </button>
      </Link>
    </div>
  );
}   