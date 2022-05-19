import { Playlist } from "./Playlist"
import { Buttons } from "../global/Buttons"
import { sendRatings } from "../../API/Recommender"

export const PlaylistPage = (props) => {
  
  const handleNext = () => {
		console.log('next');
    // const nextQuestionsNumber = questionsNumber.map(x => x + questionsNumber.length);
    // setAnswered(nextQuestionsNumber.every(x => props.answers.has(x)))
  }

  return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-5 ">
					<Playlist
						name={props.playlistName}
						setRatings={props.setRatings}
						ratings={props.ratings}
						key={props.playlistKey}
						setRatingsFilled={props.setRatingsFilled}
						trackList={props.trackList}
					/>
			</div>
			<textarea 
				className=' rounded-[2px] my-5 mt-10 border-4 border-green-500 resize-none' 
			
				placeholder="type your feedback" 
				maxLength="30" 
				cols="70" 
				rows="4" 
				wrap="hard"
				onChange={(e) => { 
					props.comment.playlistName = e.target.value;
					props.setComment(props.comment);
				}}
			/>

      <Buttons 
				{...props} 
				data={{"ratings" : props.ratings, "comment" : props.comment, "playlistName" : props.playlistName}}
				pathOnSubmit="/thanks"
				currentPath="/recommender"
				submitFunction={sendRatings} 
				answered={props.ratingsFilled} 
				onNext={handleNext}
			/>
		</div>
	)

}