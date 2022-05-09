import React, { useState } from "react";

export const StarRating = ({ startStyle, playlist, song, setRatings, ratings, setRatingsFilled }) => {  

  const [currentRating, setCurrentRating] = useState(0);
  const [hover, setHover] = useState(0);

  // const setStyleStars = (hover, rating) => {
  //   const { active, disabled, inactive } = buttonStyles;
  //   return { 
  //     className : pageCondition && answerCondition ? active : (pageCondition ? inactive : disabled),
  //     disabled : pageCondition && answerCondition === false ? true : false
  //   }
  // }
  // const starSize = "text-2xl "

  const handleRating = (idx) => {
    if (song === undefined)
      ratings.ratings[playlist].playlist = idx;
    else
      ratings.ratings[playlist].songs[song] = idx;

    setRatings(ratings);
    setCurrentRating(idx);
    setRatingsFilled(Object.values(ratings.ratings).every(x => x.playlist !== 0))
  }

  return (
    <div className="star-rating">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={ index <= (hover || currentRating) ? " text-black" : "text-slate-300"}

            onClick={() => handleRating(index)}
            onMouseEnter={() => setHover(index)}
            onMouseLeave={() => setHover(currentRating)}
          >
            <span className={ startStyle + " text-xl star"}>&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};