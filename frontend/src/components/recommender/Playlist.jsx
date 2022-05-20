import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = (props) => {

	return (
		<div>
			<h2 className="text-center">{ props.name }</h2>
			<div className=" rounded-[20px] mx-10 px-12 py-6 border-solid border-8 border-green-300 bg-gray-900 hover:border-green-500">
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
			
			<StarRating 
				{...props}
				starStyle='text-4xl text-center'
			/>
		</div>
	)
}