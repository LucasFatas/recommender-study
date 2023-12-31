import { checkEveryElementIsInMap } from "./questionnaireController";

export const optionsPerAnswer = 6;
export const ratingRange = 5;

//Orders map entries based on key
const orderMap = (map) => new Map([...map.entries()].sort());

//Shuffles content of array
export const shuffleArray = (arr) => arr ? arr.sort(() => Math.random() - 0.5) : undefined;

/**
 * Stringifies feedback object in order for it to be stored in session storage
 * @param {object} feedback feeedback object
 * @returns a string representation of the feedback object
 */
const stringifyFeedback = (feedback) => {

    return JSON.stringify({
        "personality" : {
            "questions" : Array.from(orderMap(feedback.personality.questions).entries()),
            "comment" : feedback.personality.comment
        },
        "values" : {
            "questions" : Array.from(orderMap(feedback.values.questions).entries()),
            "comment" : feedback.values.comment
        },
        "random" : {
            "questions" : Array.from(orderMap(feedback.random.questions).entries()),
            "comment" : feedback.random.comment
        }
    })
}

/**
 * Parses session object, in the initial parameter, "questions" is a 2D array.
 * Each 2D array is converted into a map and then returned.
 * @param {object} sessionFeedback object that has questions array instead of map
 * @returns 
 */
const parseSessionFeedback = (sessionFeedback) => {
    
    return {
        "personality" : {
            "questions" : new Map(sessionFeedback.personality.questions),
            "comment" : sessionFeedback.personality.comment
        },
        "values" : {
            "questions" : new Map(sessionFeedback.values.questions),
            "comment" : sessionFeedback.values.comment
        },
        "random" : {
            "questions" : new Map(sessionFeedback.random.questions),
            "comment" : sessionFeedback.random.comment
        }
    }
}

export const defaultFeedbackObj = {
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


export const defaultRatingsObj = (userId) => {
    return {
        random : { 
            playlistRating: 0, 
            songsRatings: Array(ratingRange).fill(0)
        },
        personality : { 
            playlistRating: 0, 
            songsRatings: Array(ratingRange).fill(0)
        },
        values : { 
            playlistRating: 0, 
            songsRatings: Array(ratingRange).fill(0)
        }
    }
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
        ratings[playlistName].playlistRating = idx;
        setRatingsFilled(Object.values(ratings).every(x => x.playlistRating !== 0));
    }
 
    else
        ratings[playlistName].songsRatings[song] = idx;

    setRatings(ratings);
    setCurrentRating(idx);

    sessionStorage.setItem("ratings", JSON.stringify(ratings));
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
    
    //store feedback in session storage
    sessionStorage.setItem("feedback", stringifyFeedback(feedback));
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

    //store feedback in session storage
    sessionStorage.setItem("feedback", stringifyFeedback(feedback));
    
    //Enable button to next page if all questions are answered
    setAnswered(checkEveryElementIsInMap(questionsNumberArr, currentFeedback.questions));
}


/**
 * Loads feedback object from session storage
 * @param {string} sessionFeedback feedback stored as stringified object
 * @returns feedback object
 */
export const loadFeedbackFromStorage = (sessionFeedback) => {
    const sessionObj = JSON.parse(sessionFeedback);
    return parseSessionFeedback(sessionObj);
}

/**
 * Builds data object so that it can be processed by the backend correctly.
 * @param {Number} userId user id
 * @param {Object} ratings ratings object
 * @param {Object} tracklists tracklists object
 * @param {Object} feedback feedback object
 * @returns 
 */
export const buildDataObject = (userId, ratings, tracklists, feedback) => {
    return {
        userId : userId,
        values : {
            ...ratings.values,
            matchedUserId : tracklists[0].matchedUserId,
            songUrls : tracklists[0].songs.map(x => x.spotify_url),
            comment : feedback.values.comment,
            questionFeedback : Array.from(feedback.values.questions.values())
        },
        personality : {
            ...ratings.personality,
            matchedUserId : tracklists[1].matchedUserId,
            songUrls : tracklists[1].songs.map(x => x.spotify_url),
            comment : feedback.personality.comment,
            questionFeedback : Array.from(feedback.personality.questions.values())
        },
        random : {
            ...ratings.random,
            matchedUserId : tracklists[2].matchedUserId,
            songUrls : tracklists[2].songs.map(x => x.spotify_url),
            comment : feedback.random.comment,
            questionFeedback : Array.from(feedback.random.questions.values())
        }
    }
}

export const loadFeedbackIfStored = (sessionFeedback) => sessionFeedback ? loadFeedbackFromStorage(sessionFeedback) : defaultFeedbackObj;
export const loadRatingsIfStored = (sessionRatings, userId) => sessionRatings ? JSON.parse(sessionRatings) : defaultRatingsObj(userId);
export const loadTracklistsIfStored = (sessionTracklists) => sessionTracklists ? JSON.parse(sessionTracklists) : undefined;