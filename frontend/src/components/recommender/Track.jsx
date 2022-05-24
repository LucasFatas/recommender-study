import { StarRating } from "./StarRating";

export const Track = (props) => {

  const {
    songName,
    albumName,
    artist,
    trackUrl
  } = props;

  return (
    <div className=" px-3">
      <div className="grid pt-5 pb-2 px-2 text-white" >
        <h3>Song : {songName}</h3>
        <h3>Album : {albumName}</h3>
        <h3>Artist : {artist}</h3>
      </div>
      
      <audio className="text-xl" controls src={trackUrl}/>
      <StarRating 
        {...props}
        starStyle="text-xl"
      />
		</div>
  )
}