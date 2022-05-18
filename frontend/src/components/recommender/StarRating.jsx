import React, { useState } from "react";

export const StarRating = ({ startStyle, playlist, song, setRatings, ratings, setRatingsFilled }) => {  

  const [currentRating, setCurrentRating] = useState(0);
  const [hover, setHover] = useState(0);

  const handleRating = (idx) => {
    if (song === undefined)
      ratings[playlist].playlist = idx;
    else
      ratings[playlist].songs[song] = idx;

    setRatings(ratings);
    setCurrentRating(idx);
    setRatingsFilled(Object.values(ratings).every(x => x.playlist !== 0))
  }

  return (
    <div className="star-rating text-center pt-2">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={ index <= (hover || currentRating) ? " text-yellow-500" : "text-slate-300"}

            onClick={() => handleRating(index)}
            onMouseEnter={() => setHover(index)}
            onMouseLeave={() => setHover(currentRating)}
          >
            <span className={ startStyle + " text-2xl star"}>&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};