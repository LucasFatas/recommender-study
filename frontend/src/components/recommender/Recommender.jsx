import React from "react";
import { useState } from "react";
import { Playlist } from "./Playlist";

export const Recommender = () => {

	const [ratingsFilled, setRatingsFilled] = useState(false);
	const [ratings, setRatings] = useState({
		ratings : {
			random : {
				playlist: 0, 
				songs: [0, 0, 0, 0, 0]
			},
			personality : {
				playlist: 0,
				songs: [0, 0, 0, 0, 0]
			},
			values : {
				playlist: 0,
				songs: [0, 0, 0, 0, 0]
			},
		},
		comment : ""
	})

	//TODO add textbox content to object comment

	const buttonStyles = {
		active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
		disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full",
		inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
	}


	return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-7 ">
				{['random', 'personality', 'values'].map(name => (
					<Playlist
						name={name}
						setRatings={setRatings}
						ratings={ratings}
						key={name}
						setRatingsFilled={setRatingsFilled}
					/>
				))}
			</div>
			<textarea className='mt-10 border-2 border-sky-500' placeholder="type your message" maxLength="180" cols="50" rows="6" wrap="hard"/>
			<button className={ratingsFilled ? buttonStyles.active : buttonStyles.inactive} disabled={!ratingsFilled}>Submit</button>
		</div>
	)
}