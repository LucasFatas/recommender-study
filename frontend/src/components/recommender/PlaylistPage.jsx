import { useEffect, useState } from "react";


import { Playlist } from "./Playlist"
import { Feedback } from "./Feedback";
import { Buttons } from "../global/Buttons";
import { sendRatings } from "../../API/Recommender";
import { checkEveryElementIsInMap } from "../../controller/questionnaireController";


export const PlaylistPage = (props) => {

	//const questions = props.feedback[props.playlistName].questions;

	const [answered, setAnswered] = useState(false);
	const currentFeedback = props.feedback[props.playlistName];
	const questionsNumberArr = props.questions.map((x, i) => i + 1);
	
	useEffect(() => {	
			setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
			props.setFeedback(props.feedback);
		},[currentFeedback.questions, questionsNumberArr, props] //parameters that, if changed, trigger the function above
  );

	const onAnswerChange = (e, setSelected, questionNumber, value) => {

    const questionsMap = currentFeedback.questions;
    const elementValue = e.target.value;
    const currentNumber = questionNumber + 1;

    questionsMap.set(currentNumber, parseInt(elementValue));

		//Set new state of feedback object
    props.setFeedback(props.feedback);
    
		//Set selected radio button in answer
    setSelected(questionsMap.get(currentNumber) === value);
    
		//Enable button to next page if all questions are answered
		setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
  }

	const onNext = () => console.log('gesù bastardo');

  return (
		<div className="flex flex-col items-center content-center">
			<div className='grid grid-cols-2 grid-rows-1 place-items-center mt-5'>
				<Playlist
					playlistName={props.playlistName}
					setRatings={props.setRatings}
					ratings={props.ratings}
					key={props.playlistKey}
					trackList={props.trackList}
					setRatingsFilled={props.setRatingsFilled}
				/>
				<Feedback {...props} onAnswerChange={onAnswerChange} />
			</div>
			<Buttons 
				{...props} 
				data={{"ratings" : props.ratings, "comment" : props.comment, "playlistName" : props.playlistName}}
				pathOnSubmit="/thanks"
				currentPath="/recommender"
				submitFunction={sendRatings} 
				answered={answered} 
				onNext={onNext}
			/>
		</div>
	)
}