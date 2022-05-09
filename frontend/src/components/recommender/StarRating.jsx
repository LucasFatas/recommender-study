import React, { useState } from "react";

export const StarRating = ({starSize}) => {  

  const [rating, setRating] = useState(0);
  const [hover, setHover] = useState(0);

  // const setStyleStars = (hover, rating) => {
  //   const { active, disabled, inactive } = buttonStyles;
  //   return { 
  //     className : pageCondition && answerCondition ? active : (pageCondition ? inactive : disabled),
  //     disabled : pageCondition && answerCondition === false ? true : false
  //   }
  // }
  // const starSize = "text-2xl "

  return (
    <div className="star-rating">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={ index <= (hover || rating) ? " text-black" : "text-slate-300"}

            onClick={() => setRating(index)}
            onMouseEnter={() => setHover(index)}
            onMouseLeave={() => setHover(rating)}
          >
            <span className={ starSize + " text-xl star"}>&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};