import React from "react";
import { useState } from "react";
import { RecommenderPage } from "./RecommenderPage";
import { PlaylistPage } from "./PlaylistPage";
import { Routes, Route, Navigate } from "react-router-dom";
import { PageNotFound } from "../errors/PageNotFound";

const ratingsRange = 5;

const arr = Array(5).fill({songName : "Despacito", artist : "Eminem", albumName : "The dark side of the moon", url : "https://p.scdn.co/mp3-preview/77266f8ff27e18fa575df0721323dec1509b314d?cid=8073ee0f16a64774bd0e7f8fa955b9d6%27"});

const trackLists = [
	{name : "random", list : arr},
	{name : "personality", list : arr},
	{name : "values", list : arr},
];

const lastPageIdx = trackLists.length + 1;

export const Recommender = ({ defaultPage, questions }) => {


	const [ratingsFilled, setRatingsFilled] = useState(false);

	const [comment, setComment] = useState({
		random : "",
		personality : "",
		values : "",
	});

	const [ratings, setRatings] = useState({
		random : { playlist: 0, songs: Array(ratingsRange).fill(0) },
		personality : { playlist: 0, songs: Array(ratingsRange).fill(0) },
		values : { playlist: 0, songs: Array(ratingsRange).fill(0) },
	});


	const currentPage = (trackList, idx) => {
		idx += 2;
		
		return (
			<PlaylistPage
				name={trackList.name}
				ratings={ratings}
				setRatings={setRatings}
				PlaylisyKey={idx}
				trackList={trackList.list}
				questions={questions}

				comment={comment}
				setComment={setComment}
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
				<Route path={`page${idx + 2}`} key={idx + 2} element={currentPage(tracklist, idx)} />
			))}
		</Routes>
	)
}