import React from "react";
import { useState, useEffect, useMemo } from "react";

import { Answer } from './Answer';
import { Buttons } from "../global/Buttons";
import { ProgressBar } from "./ProgressBar";
import { sendAnswer } from '../../API/Questionnaire';
import { 
  updateAnswersLogic, 
  checkEveryElementIsInMap
} from "../../controller/questionnaireController";

const legendItems = [
  'Not like me at all',
  'Not like me',
  'A little like me',
  'Somewhat like me',
  'Like me',
  'Very much like me'
]

export const QuestionnairePage = (props) => {

  const {
    answers, //Object containing maps containing answers to questionnaire
    setAnswers, //Function used to change answer
    type, //String : either 'personality' or 'values'
    numberOfPages, //Number : total number of pages
    questions, //String[] : containing all questions for the current page
    pageNumber, //Number : current page number
    pathOnSubmit, //String : path to route on submit
    optionsPerAnswer, //Number : number of radio buttons per answer
    currentPath //String : current path of the page
  } = props;

  //boolean value to check if all answers in the current page have been answered.
  const [ answered, setAnswered ] = useState(false);
  const questionsNumberArr = useMemo(() => [...questions.map(x => x[1] + 1)], [questions]);

  useEffect(() => 
    setAnswered(checkEveryElementIsInMap(questionsNumberArr, answers[type])),
    [questionsNumberArr, answers, type] //parameters that, if changed, trigger the function above
  );
    
  const updateAnswers = (e, questionNumber) => 
    updateAnswersLogic(e, questionNumber, answers, questionsNumberArr, setAnswered, setAnswers, type);

  const handleNext = () => {
    const nextQuestionsNumber = questionsNumberArr.map(x => x + questionsNumberArr.length);
    setAnswered(checkEveryElementIsInMap(nextQuestionsNumber, answers[type]));
  }

  return (
    <>
      <ProgressBar
        numberOfPages={numberOfPages}
        pageNumber={pageNumber}
      /> 
      {type === 'values' 
      ? 
      
      <ol className="mt-5 flex justify-center list-decimal list-inside mx-5">
        {legendItems.map(e => 
          <li className="mx-3" key={e}>{e}</li>  
        )}
      </ol>
    
      : ""}
      <div className='grid place-items-center'>
        {questions.map(([text, index]) => 
          <div className='flex flex-col py-10 items-center' key={index}>
            <h1 className='text-blue-500 text-center text-2xl'>{text}</h1>
            <Answer 
              answers={answers[type]} 
              questionNumber={index}  
              onChange={updateAnswers}
              optionsPerAnswer={optionsPerAnswer}
              type={type}
            />
          </div>
        )}
        <Buttons 
          {...props} 
          data={answers}
          currentPath={`/questionnaire${currentPath}`}
          pathOnSubmit={pathOnSubmit}
          submitFunction={sendAnswer}
          answered={answered} 
          onNext={handleNext}
        />
      </div>
    </>
  );
}