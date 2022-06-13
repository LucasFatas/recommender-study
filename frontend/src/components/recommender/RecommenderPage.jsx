import { useEffect } from "react";
import { Link } from "react-router-dom";

import { Playlist } from "./Playlist"

const buttonDefault = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-full text-2xl";
const buttonInactive = "select-none bg-blue-300 text-white font-bold py-2 px-5 rounded-full text-2xl";

export const RecommenderPage = (props) => {
  
	const {
		ratings, 
		setRatings, 
		ratingsFilled, 
		setRatingsFilled,
		shuffledTracklist
	} = props;

	useEffect(() => setRatingsFilled(Object.values(ratings).every(x => x.playlistRating !== 0)), [ratings, setRatingsFilled])

  return (
		<div className='h-screen w-screen grid place-items-center pt-5'>
			<div className="flex">
				{shuffledTracklist.map((e, i) => (
						<Playlist
							playlistName={e.name}
							setRatings={setRatings}
							ratings={ratings}
							key={i}
							setRatingsFilled={setRatingsFilled}
							trackList={e.songs}
						/>
					))
				}
			</div>
			<Link to="/recommender/page2" className={`${ratingsFilled ? "" : "pointer-events-none"}  pt-4 pb-8`}>
        <button className={ratingsFilled ? buttonDefault : buttonInactive} onClick={() => sessionStorage.setItem("currentUrl", "/recommender/page2")} >
          Next
        </button> 
      </Link>
		</div>
	)
}