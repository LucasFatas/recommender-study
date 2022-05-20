import { Playlist } from "./Playlist"
import { Feedback } from "./Feedback";
import { Buttons } from "../global/Buttons";
import { sendRatings } from "../../API/Recommender";


export const PlaylistPage = (props) => {

  return (
		<div className="flex flex-col items-center content-center">
			<div className='grid grid-cols-2 grid-rows-1 place-items-center mt-5'>
				<Playlist
					name={props.name}
					setRatings={props.setRatings}
					ratings={props.ratings}
					key={props.playlistKey}
					trackList={props.trackList}
				/>
				<Feedback {...props} />
			</div>
			<Buttons 
				{...props} 
				data={{"ratings" : props.ratings, "comment" : props.comment, "playlistName" : props.playlistName}}
				pathOnSubmit="/thanks"
				currentPath="/recommender"
				submitFunction={sendRatings} 
				answered={true} 
			/>
		</div>
	)

}