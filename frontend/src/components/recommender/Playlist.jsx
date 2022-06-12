import React from "react";
import { StarRating } from "./StarRating";
import { Track } from "./Track";

export const Playlist = (props) => {

	const {
		playlistName,
		trackList
	} = props;

	return (
		<div>
			<div className=" rounded-[20px] mx-10 px-16 border-solid border-8 border-green-300 bg-gray-900 hover:border-green-500">
				{trackList.map((e, idx) => (
					<div key={idx}>
						<Track 
							trackUrl= {e.preview_url}
							playlistName={playlistName} 
							song={idx} 
							songName={e.name}
							artist={e.artists}
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