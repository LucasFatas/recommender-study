import React from "react";
import { useState, useEffect } from "react";

import { RecommenderPage } from "./RecommenderPage";
import { PlaylistPage } from "./PlaylistPage";
import { Routes, Route, Navigate, useNavigate } from "react-router-dom";
import { PageNotFound } from "../errors/PageNotFound";
import questionsObj from '../../util/questions.json';
import {	loadFeedbackIfStored, loadRatingsIfStored, loadTracklistsIfStored } from "../../controller/recommenderController";
import { getSongs } from "../../API/Recommender";
import loadingGif from '../../assets/loading.gif';


const lastPageIdx = 4;
const questions = questionsObj.feedback.questions;

export const Recommender = (props) => {

	const { defaultPage } = props;

	const navigate = useNavigate()

  
  useEffect(() => {
    if(sessionStorage.getItem("currentUrl") !== "/recommender"){
      console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
      navigate(sessionStorage.getItem("currentUrl"))
    }else{
      console.log("you are in", sessionStorage.getItem("currentUrl"))
      sessionStorage.setItem("currentUrl", "/recommender/page1")
    }

  }, []);


	const [tracklists, setTracklists] = useState(loadTracklistsIfStored(sessionStorage.getItem("tracklists")));
	const [shuffledTracklist, setShuffled] = useState(loadTracklistsIfStored(sessionStorage.getItem("shuffled")))
	const [ratingsFilled, setRatingsFilled] = useState(false);
	const [loading, setLoading] = useState(true);

	useEffect(
		() => {
			if (!tracklists) 
				getSongs(sessionStorage.getItem("userID"), setTracklists, setLoading, setShuffled);
		}, [loading]
	);
	
	//Tries to retrieve feedback and ratings from storage, if they're not stored the defaultObject is used.
	const [feedback, setFeedback] = useState(loadFeedbackIfStored(sessionStorage.getItem("feedback")));
	const [ratings, setRatings] = useState(loadRatingsIfStored(sessionStorage.getItem("ratings")));


	const loadingComponent = (
		<div className="w-screen h-screen flex justify-center items-center">
			<img src={loadingGif} alt="loading"/>
		</div>
	);

	const currentPage = (trackList, idx) => {

		return (
			<PlaylistPage
				playlistName={trackList.name}
				ratings={ratings}
				setRatings={setRatings}
				PlaylisyKey={idx}
				trackList={trackList.songs}
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
		shuffledTracklist={shuffledTracklist}
			ratings={ratings}
			setRatings={setRatings}
			ratingsFilled={ratingsFilled}
			setRatingsFilled={setRatingsFilled}
			loading={loading}
			loadingComponent={loadingComponent}
		/>
	);

	return (
		<Routes>
			<Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
			<Route path="/" element={<Navigate replace to="page1"/>} />
			<Route path="page1" element={shuffledTracklist ? recommenderPage : loadingComponent} />
			{[2, 3, 4].map((e, idx) => (
				<Route path={`page${e}`} exact key={e} element={shuffledTracklist ? currentPage(shuffledTracklist[idx], e) : loadingComponent} />
			))}
		</Routes>
	)
}