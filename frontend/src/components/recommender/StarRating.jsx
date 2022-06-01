import React, { useEffect, useState } from "react";

import { handleRating } from "../../controller/recommenderController";

export const StarRating = (props) => {  

  const { 
    starStyle, //String containing CSS style of the star buttons
    playlistName, //String with playlist name, either 'random', 'personality' or 'values'
    song, //Number containing index of current song
    setRatings, //Function to change ratings object
    ratings,  //Object, to see structure go to recommenderController and check initialRatingsObj
    setRatingsFilled  //Function to change value of boolean ratingsFilled
  } = props;

  //Hover caused issues with the code. Might be reimplemented later on.
  //const [hover, setHover] = useState(0);
  const [currentRating, setCurrentRating] = useState(song === undefined ? ratings[playlistName].playlist : ratings[playlistName].songs[song]);

  useEffect(() => {
      if (song === undefined) 
        setCurrentRating(ratings[playlistName].playlist);
      else 
        setCurrentRating(ratings[playlistName].songs[song]);
    }, [song, ratings, playlistName]
  );

  return (
    <div className="star-rating text-center pt-2">
      {[...Array(5)].map((star, index) => {
        index += 1;
        return (
          <button
            type="button"
            key={index}
            className={ index <= currentRating ? " text-yellow-500" : "text-slate-300"}

            onClick={() => handleRating(index, ratings, song, playlistName, setRatingsFilled, setRatings, setCurrentRating)}
            /* onMouseEnter={() => setHover(index)} */
            /* onMouseLeave={() => setHover(currentRating)} */
          >
            <span className={ starStyle + " text-2xl star"}>&#9733;</span>
          </button>
        );
      })}
    </div>
  );
};