export const optionsPerAnswer = 6;
export const ratingRange = 5;

export const initialFeedbackObj = {
    random : {
        questions : new Map(),
        comment : ""
    },
    personality : {
        questions : new Map(),
        comment : ""
    },
    values : {
        questions : new Map(),
        comment : ""
    }
}

const ratingsRange = 5;

export const initialRatingsObj = {
    random : { playlist: 0, songs: Array(ratingsRange).fill(0) },
    personality : { playlist: 0, songs: Array(ratingsRange).fill(0) },
    values : { playlist: 0, songs: Array(ratingsRange).fill(0) },
}

export const handleRating = (idx, ratings, song, playlistName, setRatingsFilled, setRatings, setCurrentRating) => {
    if (song === undefined) {
        ratings[playlistName].playlist = idx;
        setRatingsFilled(Object.values(ratings).every(x => x.playlist !== 0));
    }
 
    else
        ratings[playlistName].songs[song] = idx;

    setRatings(ratings);
    setCurrentRating(idx);
}