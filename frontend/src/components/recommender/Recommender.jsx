import React from "react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { Playlist } from "./Playlist";
import { sendRatings } from "../../API/Recommender";

export const Recommender = () => {

	const navigate = useNavigate();

	
	const defaultValues = Array(5).fill(0);

	const [comment, setComment] = useState("");
	const [ratingsFilled, setRatingsFilled] = useState(false);
	const [ratings, setRatings] = useState({
		random : { playlist: 0, songs: defaultValues },
		personality : { playlist: 0, songs: defaultValues },
		values : { playlist: 0, songs: defaultValues },
	})

	//TODO extract button styles somewhere else and use them for the questionnaire button too
	const buttonStyles = {
		active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
		disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full",
		inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
	}

	const arr = Array(5).fill(
		{songName : "Despacito", artist : "Eminem", albumName : "The dark side of the moon", url : "https://p.scdn.co/mp3-preview/77266f8ff27e18fa575df0721323dec1509b314d?cid=8073ee0f16a64774bd0e7f8fa955b9d6%27"});
	const trackLists = [
		{name : "random", list : arr},
		{name : "personality", list : arr},
		{name : "values", list : arr},
	]

	const handleSubmit = () => {
		sendRatings({"ratings" : ratings, "comment" : comment});
		navigate('/thanks');
	}

	return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-5 ">
				{trackLists.map((trackList, idx) => (
					<Playlist
						name={trackList.name}
						setRatings={setRatings}
						ratings={ratings}
						key={idx}
						setRatingsFilled={setRatingsFilled}
						trackList={trackList.list}
					/>
				))}
			</div>
			<textarea 
				className=' rounded-[2px] my-5 mt-10 border-4 border-green-500 resize-none' 
			
				placeholder="type your feedback" 
				maxLength="30" 
				cols="70" 
				rows="4" 
				wrap="hard"
				onChange={(e) => setComment(e.target.value)}
			/>
			<button 
				className={ratingsFilled ? buttonStyles.active : buttonStyles.inactive} 
				disabled={!ratingsFilled}
				onClick={handleSubmit}
			>
				Submit
			</button>
		</div>
	)
}