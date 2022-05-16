import { Playlist } from "./Playlist"

export const RecommenderPage = (props) => {


  const handleSubmit = () => {

  }

  
  //TODO extract button styles somewhere else and use them for the questionnaire button too
  const buttonStyles = {
    active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
    disabled : "select-none text-transparent fonted bg-transparent hover:bg-transparent py-2 px-4 rounded-full",
    inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full "
  }

  return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit mt-10 space-x-5 ">
					<Playlist
						name={props.name}
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
				onChange={(e) => props.setComment(e.target.value)}
			/>
			<button 
				className={props.ratingsFilled ? buttonStyles.active : buttonStyles.inactive} 
				disabled={!props.ratingsFilled}
				onClick={handleSubmit}
			>
				Submit
			</button>
		</div>
	)

}