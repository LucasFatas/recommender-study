import { checkEveryElementIsInMap } from "./questionnaireController";

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

export const initialRatingsObj = {
    random : { playlist: 0, songs: Array(ratingRange).fill(0) },
    personality : { playlist: 0, songs: Array(ratingRange).fill(0) },
    values : { playlist: 0, songs: Array(ratingRange).fill(0) },
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

export const handleComment = (e, currentFeedback, feedback, setFeedback, playlistName) => {
    currentFeedback.comment = e.target.value;
    setFeedback({...feedback, [playlistName] : { ...currentFeedback}});
}

export const updateAnswersLogic = (e, questionNumber, feedback, setFeedback, currentFeedback, setAnswered, questionsNumberArr) => {

    const questionsMap = currentFeedback.questions;
    const elementValue = e.target.value;
    const currentNumber = questionNumber + 1;

    questionsMap.set(currentNumber, parseInt(elementValue));

    //Set new state of feedback object
    setFeedback(feedback);
    
    //Enable button to next page if all questions are answered
    setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
}