import { useEffect, useState } from "react";


import { Playlist } from "./Playlist"
import { Feedback } from "./Feedback";
import { Buttons } from "../global/Buttons";
import { sendRatings } from "../../API/Recommender";
import { checkEveryElementIsInMap } from "../../controller/questionnaireController";
import { updateAnswersLogic } from "../../controller/recommenderController";


export const PlaylistPage = (props) => {

	const [answered, setAnswered] = useState(false);

	const {
		feedback, //Object, check recommenderController inintialFeedbackObj for structure
		setFeedback, //Function to change feedback object
		playlistName, //String with playlist name
		questions, //String[] containing feedback questions text
		ratings, //Object, check recommenderController initialRatingsObj for structure
		setRatings, //Function to change ratings object
		trackList, //Object[] check Recommender.jsx for structure
		setRatingsFilled, //Function to change ratingsFilled parameter
		comment //String containing feedback comment on current page
	} = props;

	const currentFeedback = feedback[playlistName];
	const questionsNumberArr = questions.map((x, i) => i + 1);
	
	useEffect(() => {	
			setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
			setFeedback(feedback);
		},[currentFeedback.questions, questionsNumberArr, props] //parameters that, if changed, trigger the function above
  );

	const onAnswerChange = (e, questionNumber) => updateAnswersLogic(e, questionNumber, feedback, setFeedback, currentFeedback, setAnswered, questionsNumberArr);

  return (
		<div className="flex flex-col items-center content-center">
			<div className='grid grid-cols-2 grid-rows-1 place-items-center mt-5'>
				<Playlist
					playlistName={playlistName}
					setRatings={setRatings}
					ratings={ratings}
					trackList={trackList}
					setRatingsFilled={setRatingsFilled}
				/>
				<Feedback {...props} onAnswerChange={onAnswerChange} />
			</div>
			<Buttons 
				{...props} 
				data={{"ratings" : ratings, "comment" : comment, "playlistName" : playlistName}}
				pathOnSubmit="/thanks"
				currentPath="/recommender"
				submitFunction={sendRatings} 
				answered={answered}
			/>
		</div>
	)
}