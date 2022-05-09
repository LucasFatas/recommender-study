import React from "react";
import { StarRating } from "./StarRating";

export const Playlist = (props) => {

	return (
		<div>
			<h2>{ props.name }</h2>
			<div>
				{[...Array(5)].map((e, idx) => (
					<div key={idx}>
						<h3>Song {idx + 1}</h3>
						<StarRating 
							startStyle="text-xl" 
							playlist={props.name} 
							song={idx} 
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