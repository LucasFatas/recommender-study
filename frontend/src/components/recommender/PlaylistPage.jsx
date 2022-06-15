import { useEffect, useState } from "react";

import { Playlist } from "./Playlist"
import { Feedback } from "./Feedback";
import { Buttons } from "../global/Buttons";
import { sendRatings } from "../../API/Recommender";
import { checkEveryElementIsInMap } from "../../controller/questionnaireController";
import { updateAnswersLogic } from "../../controller/recommenderController";
import { useNavigate } from "react-router-dom";
import { PlaylistPageSecurity } from "../../controller/pathSecurityController";


export const PlaylistPage = (props) => {

	const [answered, setAnswered] = useState(false);

	const {
		feedback,
		setFeedback,
		playlistName,
		questions,
		ratings,
		setRatings,
		playlistKey,
		trackList,
		setRatingsFilled,
		comment,
		nextPage
	} = props;

	const currentFeedback = feedback[playlistName];
	const questionsNumberArr = questions.map((x, i) => i + 1);

	const navigate = useNavigate()

  useEffect(() => {
    PlaylistPageSecurity(navigate)

  }, []);
	
	useEffect(() => {	
			setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
			setFeedback(feedback);
		},[currentFeedback.questions, questionsNumberArr, props, feedback, setFeedback] //parameters that, if changed, trigger the function above
  );

	const onAnswerChange = (e, questionNumber) => updateAnswersLogic(e, questionNumber, feedback, setFeedback, currentFeedback, setAnswered, questionsNumberArr);

  return (
		<div className="w-screen h-screen flex flex-col items-center content-center py-4 pb-32">
			<div className='grid grid-cols-3 grid-rows-1 place-items-center'>
				<Playlist
					playlistName={playlistName}
					setRatings={setRatings}
					ratings={ratings}
					key={playlistKey}
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
				submitFunction={() => sendRatings(ratings, feedback)}
				submitResults={playlistName === 'random'}
				answered={answered}
				onNext={() => sessionStorage.setItem("currentUrl", "/recommender/page" + (nextPage))}
			/>
		</div>
	)
}