import { useEffect } from "react";
import { Link } from "react-router-dom";

import { Playlist } from "./Playlist"

const { buttonDefault, buttonInactive } = require('../../util/style.json');

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
        <button className={ratingsFilled ? buttonDefault : buttonInactive}>
          Next
        </button> 
      </Link>
		</div>
	)
}