export const optionsPerAnswer = 6;

export const getProgressPercentage = (pageNumber, totalPages) => pageNumber / totalPages * 100;

/** 
   * Splits the array of questions into a 2D array where each row is an 
   * array of questions that is going to appear on one page.
   * The number of rows always equals the number of pages in the questionnaire.
*/
export const splitArrayIntoMatrix = (array, rowSize) => {
    return array.map((e, i) => {
        return i % rowSize === 0 ? array.slice(i, i + rowSize).map((e, idx) => [e, i + idx]) : null;
    }).filter(e => { return e; });
}

export const checkEveryElementIsInMap = (array, map) => array.every(x => map.has(x));

export const updateAnswersLogic = (element, questionNumber, answers, questionsNumberArr, setAnswered, setAnswers) => {

    const elementValue = element.target.value;
    const currentNumber = questionNumber + 1;

    //Set solution in answers map
    setAnswers(answers.set(currentNumber, parseInt(elementValue)));
    
    //Enable button to next page if all questions are answered
    setAnswered(questionsNumberArr.every(x => answers.has(x)));
}
