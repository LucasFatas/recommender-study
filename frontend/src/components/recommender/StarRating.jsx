import React, { useEffect, useState } from "react";

export const StarRating = ({ starStyle, name, song, setRatings, ratings, setRatingsFilled, initialRating }) => {  

  const [hover, setHover] = useState(0);
  const [currentRating, setCurrentRating] = useState(0);

  useEffect(() => 
    {
      if (song === undefined) 
        setCurrentRating(ratings[name].playlist);
      else 
        setCurrentRating(ratings[name].songs[song]);
    }
  );

  const handleRating = (idx) => {
    
    if (song === undefined) {
      ratings[name].playlist = idx;
      setRatingsFilled(true);
    }
    else
      ratings[name].songs[song] = idx;

    setRatings(ratings);
    setCurrentRating(idx);
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
            <span className={ starStyle + " text-2xl star"}>&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};