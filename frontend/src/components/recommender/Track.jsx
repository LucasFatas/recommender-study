import React from "react";
import { StarRating } from "./StarRating";

export const Track = (props) => {
  return (
    <div className=" px-3">
      <div className="grid pt-5 pb-2 px-2 text-white" >
        <h3>Song : {props.songName}</h3>
        <h3>Album : {props.albumName}</h3>
        <h3>Artist : {props.artist}</h3>
      </div>
      
      <audio className="text-xl" controls src={props.trackUrl}/>
      <StarRating startStyle="text-xl"  {...props} />
		</div>
  )
}