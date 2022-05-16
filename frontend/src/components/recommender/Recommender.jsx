import React from "react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { sendRatings } from "../../API/Recommender";
import { RecommenderPage } from "./RecommenderPage";
import { Routes, Route, Navigate } from "react-router-dom";
import { PageNotFound } from "../errors/PageNotFound";

export const Recommender = ({defaultPage}) => {

	const navigate = useNavigate();

	
	const defaultValues = Array(5).fill(0);

	const [comment, setComment] = useState("");
	const [ratingsFilled, setRatingsFilled] = useState(false);
	const [ratings, setRatings] = useState({
		random : { playlist: 0, songs: defaultValues },
		personality : { playlist: 0, songs: defaultValues },
		values : { playlist: 0, songs: defaultValues },
	})

	

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

	const currentPage = (trackList, idx) => (
		<RecommenderPage
		playlistName={trackList.name}
		setRatings={setRatings}
		ratings={ratings}
		PlaylisyKey={idx}
		ratingsFilled={ratingsFilled}
		setRatingsFilled={setRatingsFilled}
		trackList={trackList.list}

		setComment={setComment}
	
		/>
	)

	return (
		<Routes>
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
        <Route path="/" element={<Navigate replace to="page1"/>} />
        {
          trackLists.map((tracklist, idx) => (
            <Route path={`page${idx + 1}`} key={idx + 1} element={currentPage(tracklist, idx)}/>
          ))
        }
      </Routes>

	)
	// 	<div className='grid place-items-center'>
	// 		<div className="flex justify-center w-fit mt-10 space-x-5 ">
	// 			{trackLists.map((trackList, idx) => (
	// 				<Playlist
	// 					name={trackList.name}
	// 					setRatings={setRatings}
	// 					ratings={ratings}
	// 					key={idx}
	// 					setRatingsFilled={setRatingsFilled}
	// 					trackList={trackList.list}
	// 				/>
	// 			))}
	// 		</div>
	// 		<textarea 
	// 			className=' rounded-[2px] my-5 mt-10 border-4 border-green-500 resize-none' 
			
	// 			placeholder="type your feedback" 
	// 			maxLength="30" 
	// 			cols="70" 
	// 			rows="4" 
	// 			wrap="hard"
	// 			onChange={(e) => setComment(e.target.value)}
	// 		/>
	// 		<button 
	// 			className={ratingsFilled ? buttonStyles.active : buttonStyles.inactive} 
	// 			disabled={!ratingsFilled}
	// 			onClick={handleSubmit}
	// 		>
	// 			Submit
	// 		</button>
	// 	</div>
	// )
}