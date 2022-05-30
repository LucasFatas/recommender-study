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

/**
 * Handles all the ratings relative to the recommender.
 * @param {number} idx index of the radio button
 * @param {object} ratings ratings object
 * @param {?number} song song number
 * @param {string} playlistName playlist name
 * @param {function} setRatingsFilled function to set ratingsFilled to true if conditions are met
 * @param {function} setRatings function to change the ratings object
 * @param {function} setCurrentRating function to set the current rating
 */
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


/**
 * Handles the logic behind adding a feedback comment
 * @param {object} e current DOM element
 * @param {object} currentFeedback current feedback object
 * @param {object} feedback complete feedback object
 * @param {function} setFeedback function to change feedback object
 * @param {string} playlistName playlist name
 */
export const handleComment = (e, currentFeedback, feedback, setFeedback, playlistName) => {
    
    currentFeedback.comment = e.target.value;
    setFeedback({...feedback, [playlistName] : { ...currentFeedback}});
}


/**
 * Handles the logic behind the feedback answers
 * @param {object} e current DOM element
 * @param {number} questionNumber current question number
 * @param {object} feedback complete feedback object
 * @param {function} setFeedback function to change the feedback object
 * @param {object} currentFeedback current feedbak object
 * @param {function} setAnswered function to set answered parameter to true if conditions are met
 * @param {number[]} questionsNumberArr array with the numbers of the questions
 */
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