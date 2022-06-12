import { StarRating } from "./StarRating";

export const Track = (props) => {

  const {
    songName,
    artist,
    trackUrl
  } = props;

  return (
    <div className="px-3">
      <div className="grid py-3 mt-3 text-center text-white" >
        <h3>Song : {songName}</h3>
        <h3>Artist : {artist.join(', ')}</h3>
      </div>
      
      <audio className="text-xl" controls src={trackUrl}/>
      <StarRating 
        {...props}
        starStyle="text-xl"
      />
		</div>
  )
}