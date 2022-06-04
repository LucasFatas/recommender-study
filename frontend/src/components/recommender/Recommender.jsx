import React from "react";
import { useState, useEffect } from "react";
import { RecommenderPage } from "./RecommenderPage";
import { PlaylistPage } from "./PlaylistPage";
import { Routes, Route, Navigate } from "react-router-dom";
import { PageNotFound } from "../errors/PageNotFound";
import questionsObj from '../../util/questions.json';
import { 
	initialRatingsObj, 
	initialFeedbackObj,
	loadFeedbackFromStorage
} from "../../controller/recommenderController";
import { getSongs } from "../../API/Recommender";

//TODO : remove once we can retrieve songs from user
const arr = Array(5).fill({songName : "Despacito", artist : "Eminem", albumName : "The dark side of the moon", url : "https://p.scdn.co/mp3-preview/77266f8ff27e18fa575df0721323dec1509b314d?cid=8073ee0f16a64774bd0e7f8fa955b9d6%27"});

const trackLists = [
	{name : "random", list : arr},
	{name : "personality", list : arr},
	{name : "values", list : arr},
];

const lastPageIdx = trackLists.length + 1;

export const Recommender = (props) => {
	
	useEffect(() => {
		const userId = sessionStorage.getItem("userID");
		getSongs(userId)
	});
	
	const { defaultPage } = props;
	
	const questions = questionsObj.feedback.questions;
	const sessionRatings = sessionStorage.getItem("ratings");
	const sessionFeedback = sessionStorage.getItem("feedback");

	const [ratingsFilled, setRatingsFilled] = useState(false);

	const [feedback, setFeedback] = useState(
		sessionFeedback === null 
		? initialFeedbackObj
		: loadFeedbackFromStorage(sessionFeedback) 
	);

	const [ratings, setRatings] = useState(
		sessionRatings === null
		? initialRatingsObj
		: JSON.parse(sessionRatings)
	);


	const currentPage = (trackList, idx) => {
		idx += 2; //Accounts for pages starting at 1 and the first page being RecommenderPage

		return (
			<PlaylistPage
				playlistName={trackList.name}
				ratings={ratings}
				setRatings={setRatings}
				PlaylisyKey={idx}
				trackList={trackList.list}
				questions={questions}
				answers={feedback[trackList.name].questions}
				setRatingsFilled={setRatingsFilled}

				feedback={feedback}
				setFeedback={setFeedback}
				pageNumber={idx}
				prevPage={idx === 1 ? false : idx - 1} 
				nextPage={idx === lastPageIdx ? false : idx + 1}
				showSubmit={idx === lastPageIdx ? 3 : false}
			/>
		)
	};

	const recommenderPage = (
		<RecommenderPage 
			trackLists={trackLists} 
			ratings={ratings}
			setRatings={setRatings}
			ratingsFilled={ratingsFilled}
			setRatingsFilled={setRatingsFilled}
		/>
	)

	return (
		<Routes>
			<Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
			<Route path="/" element={<Navigate replace to="page1"/>} />
			<Route path="page1" element={recommenderPage} />
			{trackLists.map((tracklist, idx) => (
				<Route path={`page${idx + 2}`} exact key={idx + 2} element={currentPage(tracklist, idx)} />
			))}
		</Routes>
	)
}