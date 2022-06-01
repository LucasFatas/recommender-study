import { useEffect } from "react";
import { Link } from "react-router-dom";

import { Playlist } from "./Playlist"

const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full"
}

export const RecommenderPage = (props) => {
  
	const {
		trackLists, //Object[] check Recommender.jsx for structure
		ratings, //Object check recommenderController initialRatingsObj for structure
		setRatings, //Function to change ratings object
		ratingsFilled, //boolean, true if all playlist ratings are answered, false otherwise
		setRatingsFilled //Function to change value of ratingsFilled 
	} = props;

	useEffect(() => setRatingsFilled(Object.values(ratings).every(x => x.playlist !== 0)), [ratings, setRatingsFilled])

  return (
		<div className='grid place-items-center'>
			<div className="flex justify-center w-fit h-fit mt-5 space-x-5 ">
				{trackLists.map((e, i) => (
					<Playlist
						playlistName={e.name}
						setRatings={setRatings}
						ratings={ratings}
						key={i}
						setRatingsFilled={setRatingsFilled}
						trackList={e.list}
					/>
				))}
			</div>
			<Link to="/recommender/page2" className={ratingsFilled ? "mt-5" : "mt-5 pointer-events-none"}>
        <button className={ratingsFilled ? buttonStyles.active : buttonStyles.inactive}>
          Next
        </button> 
      </Link>
		</div>
	)

}