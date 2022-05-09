import React from "react";
import { StarRating } from "./StarRating";

export const Track = ({starSize, trackUrl}) =>{
  console.log(trackUrl)

  return (
    <div>
      <iframe className="" src={trackUrl} width="100%" height="80" frameBorder="0" allowfullscreen="" title="music" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
      <StarRating
      starSize={starSize}
      />
		</div>
  )
}