import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = (props) => {
	const trackList = props.trackList
	console.log(props.trackList)
	return (
		<div>
			<h2>{ props.name }</h2>
			<div>
				{trackList.map((e, idx) => (
					<div key={idx}>
						<h3>Song {idx + 1}</h3>
						<Track 
							trackUrl= {e}
							startStyle="text-xl" 
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