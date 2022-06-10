import { useEffect, useState } from "react";

import { Playlist } from "./Playlist"
import { Feedback } from "./Feedback";
import { Buttons } from "../global/Buttons";
import { sendRatings } from "../../API/Recommender";
import { checkEveryElementIsInMap } from "../../controller/questionnaireController";
import { updateAnswersLogic } from "../../controller/recommenderController";
import { useNavigate } from "react-router-dom";


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
    const url = sessionStorage.getItem("currentUrl")
    if(url.includes("/recommender")){
      const endOfToken = parseInt(url.replace("/recommender/page", "").replaceAll(" ", ""));
      console.log(endOfToken + typeof endOfToken)
      if(!Number.isNaN(endOfToken) && endOfToken < (nextPage - 1)){
        console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
        navigate(sessionStorage.getItem("currentUrl"))
      }
    }else {
     
      console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
      navigate(sessionStorage.getItem("currentUrl"))
    }

  }, []);
	
	useEffect(() => {	
			setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
			setFeedback(feedback);
		},[currentFeedback.questions, questionsNumberArr, props, feedback, setFeedback] //parameters that, if changed, trigger the function above
  );

	const onAnswerChange = (e, questionNumber) => updateAnswersLogic(e, questionNumber, feedback, setFeedback, currentFeedback, setAnswered, questionsNumberArr);

  return (
		<div className="flex flex-col items-center content-center">
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