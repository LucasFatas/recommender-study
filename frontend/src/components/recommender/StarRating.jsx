import React, { useEffect, useState } from "react";

import { handleRating } from "../../controller/recommenderController";

export const StarRating = ({ starStyle, playlistName, song, setRatings, ratings, setRatingsFilled, initialRating }) => {  

  const [hover, setHover] = useState(0);
  const [currentRating, setCurrentRating] = useState(0);

  useEffect(() => {
      if (song === undefined) 
        setCurrentRating(ratings[playlistName].playlist);
      else 
        setCurrentRating(ratings[playlistName].songs[song]);
    }
  );

  return (
    <div className="star-rating text-center pt-2">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={ index <= (hover || currentRating) ? " text-yellow-500" : "text-slate-300"}

            onClick={() => handleRating(index, ratings, song, playlistName, setRatingsFilled, setRatings, setCurrentRating)}
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