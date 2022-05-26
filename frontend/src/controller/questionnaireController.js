export const getProgressPercentage = (pageNumber, totalPages) => pageNumber / totalPages * 100;

export const getRandomValue = (arr) => arr[Math.floor(Math.random() * arr.length)];

export const checkEveryElementIsInMap = (array, map) => array.every(x => map.has(x));

/**
 * Splits the array into a 2d array based on the rowsize
 * @param {string[]} array array to be split in rows
 * @param {number} rowSize the row size
 * @returns a 2d array with the same content of the 
 * original array but with the content split into rows.
 */
export const splitArrayIntoMatrix = (array, rowSize) => {
    return array.map((e, i) => {
        return i % rowSize === 0 ? array.slice(i, i + rowSize).map((e, idx) => [e, i + idx]) : null;
    }).filter(e => { return e; });
}


/**
 * Takes the answers object and orders the entries of the 
 * maps based on the indexes.
 * @param {{personality : Map, values : Map}} answers answers object
 * @returns The same answers object but with ordered maps.
 */
const orderAnswers = (answers) => {
    return {
        "personality" : new Map([...answers.personality.entries()].sort()),
        "values" : new Map([...answers.values.entries()].sort())
    }
}


/**
 * Takes the answers object and converts it into a 
 * stringified version that can be stored in the sessionStorage
 * @param {{personality : Map, values : Map}} answers the answers object
 * @returns The stringified object
 */
export const stringifyAnswers = (answers) => {
    const orderedAnswers = orderAnswers(answers);
    
    return JSON.stringify({
        "personality" : Array.from(orderedAnswers.personality.entries()), 
        "values" : Array.from(orderedAnswers.values.entries())
    });
}


/**
 * Parses the session object into the answer object used in the useState
 * @param {{personality : string[][], values : string[][]}} obj 
 * object containing 2d array of size nx2 where n is
 * the number of questions and each item will become an entry
 * in a map where the first value is used as the key and the second as 
 * the value.
 * @returns parsed object
 */
export const parseSessionObj = (obj) => {
    return {
        "personality" : new Map(obj.personality),
        "values" : new Map(obj.values)
    }
}


/**
 * Updates the answers object, checks if all questions in a page 
 * are answered and save the answers in the session storage.
 * @param {object} element DOM element clicked
 * @param {number} questionNumber Question number of the current answer
 * @param {{personality : Map, values : Map}} answers Anaswers object
 * @param {number[]} questionsNumberArr 
 * @param {function} setAnswered 
 * @param {function} setAnswers 
 * @param {string} type 
 */
export const updateAnswersLogic = (element, questionNumber, answers, questionsNumberArr, setAnswered, setAnswers, type) => {

    const elementValue = element.target.value;
    const currentNumber = questionNumber + 1;


    console.log(questionsNumberArr)
    
    //Set solution in answers map
    answers[type].set(currentNumber, parseInt(elementValue))
    setAnswers(orderAnswers(answers));

    //Save answers in session storage
    window.sessionStorage.setItem("answers", stringifyAnswers(answers));
    
    //Enable button to next page if all questions are answered
    setAnswered(questionsNumberArr.every(x => answers[type].has(x)));
}


/**
 * Checks if answers are stored in session storage, 
 * if they are parse and return them.
 * @param {?string} sessionAnswers stringified object that can be null
 * @returns the parsed object with the answer maps
 */
export const loadAnswersFromStorage = (sessionAnswers) => {
    if (sessionAnswers) {
      const sessionObj = JSON.parse(sessionAnswers);
      return parseSessionObj(sessionObj);
    }
}


/**
 * Check if the first questionnaire is already selected
 * if it isn't, generate one and save in session storage.
 * @param {?string} options 
 * @returns 'personality' if personality is the first questionnaire, 'values' otherwise.
 */
export const getRandomQuestionnaire = (options) => {
    const selectedQuestionnaire = sessionStorage.getItem("firstQuestionnaire");

    if (selectedQuestionnaire === null) {
        const choice = getRandomValue(options);
        sessionStorage.setItem("firstQuestionnaire", choice);
        return choice;
    } else 
        return selectedQuestionnaire;
    
}