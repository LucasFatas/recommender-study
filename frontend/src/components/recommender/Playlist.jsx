import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = (props) => {

	return (
		<div>
			<h2>{ props.name }</h2>
			<div>
				{props.trackList.map((e, idx) => (
					<div key={idx}>
						<h3>Song {idx + 1}</h3>
						<Track 
							trackUrl= {e}
							playlist={props.name} 
							song={idx} 
							idx={idx}
							key={idx}
							{...props}
						/>
					</div>
				))}
			</div>
			
			<StarRating startStyle='text-2xl text-center' playlist={props.name} {...props}/>
		</div>
	)
}