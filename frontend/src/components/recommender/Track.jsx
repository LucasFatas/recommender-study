import React from "react";
import { StarRating } from "./StarRating";

export const Track = (props) => {
  return (
    <div>
      <iframe className="" src={props.trackUrl} width="100%" height="80" frameBorder="0" allowFullScreen="" title="music" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"/>
      <StarRating startStyle="text-xl"  {...props} />
		</div>
  )
}