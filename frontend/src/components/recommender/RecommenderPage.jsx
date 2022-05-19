import { Link, useNavigate } from 'react-router-dom';

import { Playlist } from "./Playlist"
import { Buttons } from "../global/Buttons"
import { sendRatings } from "../../API/Recommender"

export const RecommenderPage = (props) => {
  
	const {trackLists, ratings, setRatings, ratingsFilled, setRatingsFilled } = props;

  const handleNext = () => {
		console.log('next');
    // const nextQuestionsNumber = questionsNumber.map(x => x + questionsNumber.length);
    // setAnswered(nextQuestionsNumber.every(x => props.answers.has(x)))
  }

  return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-5 ">
					{trackLists.map((e, i) => (
						<Playlist
							name={e.name}
							setRatings={setRatings}
							ratings={ratings}
							key={i}
							setRatingsFilled={setRatingsFilled}
							trackList={e.list}
						/>
					))}
			</div>

			<Buttons
				pathOnSubmit="/thanks"
				currentPath="/recommender"
				ratings={ratings}
				setRatings={setRatings}
				setRatingsFilled={setRatingsFilled}			
				submitFunction={sendRatings} 
				answered={ratingsFilled} 
				onNext={handleNext}
			/>
		</div>
	)

}