import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = (props) => {

	return (
		<div>
			<h2 className="text-center">{ props.name }</h2>
			<div className=" rounded-[20px] border-solid border-8 border-green-300 bg-gray-900 hover:border-green-500">
				{props.trackList.map((e, idx) => (
					<div key={idx}>
						<Track 
							trackUrl= {e.url}
							playlist={props.name} 
							song={idx} 
							songName={e.songName}
							artist={e.artist}
							albumName={e.albumName}
							idx={idx}
							key={idx}
							{...props}
						/>
					</div>
				))}
			</div>
			
			<StarRating startStyle='text-4xl text-center' playlist={props.name} initialRating={props.ratings[props.name].playlist} {...props}/>
		</div>
	)
}