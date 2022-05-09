import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = ({name, starSize, trackList}) => {

	console.log(trackList);

	return (
		<div>
			<h2>{ name }</h2>
			{trackList.map((trackUrl, index) => 
          <Track 
					starSize={starSize}
					trackUrl= {trackUrl}
					/>
        )}
			<StarRating
				starSize={'text-2xl text-center'}
			/>
		</div>
	)
}