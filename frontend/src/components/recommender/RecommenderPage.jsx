import { Link } from "react-router-dom";

import { Playlist } from "./Playlist"

const buttonStyles = {
  active : "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ",
  inactive : "select-none bg-blue-300 text-white font-bold py-2 px-4 rounded-full pointer-events-none"
}

export const RecommenderPage = (props) => {
  
	const {trackLists, ratings, setRatings, ratingsFilled, setRatingsFilled } = props;

	setRatingsFilled(Object.values(ratings).every(x => x.playlist !== 0));

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

			
			<Link to="/recommender/page2" className="mt-5">
        <button className={ratingsFilled ? buttonStyles.active : buttonStyles.inactive}>
          Next
        </button> 
      </Link>
		</div>
	)

}