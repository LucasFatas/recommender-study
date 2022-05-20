import React from "react";
import { useState, useEffect, useMemo } from "react";

import { Answer } from './Answer';
import { Buttons } from "../global/Buttons";
import { ProgressBar } from "./ProgressBar";
import { sendAnswer } from '../../API/Questionnaire';
import { updateAnswersLogic, checkEveryElementIsInMap } from "../../controller/questionnaireController";

export const QuestionnairePage = (props) => {
  
  //boolean value to check if all answers in the current page have been answered.
  const [ answered, setAnswered ] = useState(false);
  const questionsNumberArr = useMemo(() => [...props.questions.map(x => x[1] + 1)], [props.questions]);

  useEffect(() => 
    setAnswered(checkEveryElementIsInMap(questionsNumberArr, props.answers)),
    [questionsNumberArr, props.answers] //parameters that, if changed, trigger the function above
    );
    
  const updateAnswers = (e, setSelected, questionNumber, value) => 
    updateAnswersLogic(e, setSelected, questionNumber, value, props.answers, questionsNumberArr, setAnswered, props.setAnswers);

  const handleNext = () => {
    const nextQuestionsNumber = questionsNumberArr.map(x => x + questionsNumberArr.length);
    setAnswered(checkEveryElementIsInMap(nextQuestionsNumber, props.answers));
  }

  return (
    <>
      <ProgressBar
        numberOfPages={props.numberOgPages}
        pageNumber={props.pageNumber}
      /> 
      <div className='grid place-items-center'>
        {props.questions.map(([text, index]) => 
          <div className='flex flex-col py-10 items-center' key={index}>
            <h1 className='text-blue-500 text-center text-2xl'>{text}</h1>
            <Answer 
              answers={props.answers} 
              questionNumber={index}  
              onChange={updateAnswers}
            />
          </div>
        )}
        <Buttons 
          {...props} 
          data={props.answers}
          currentPath="/questionnaire"
          pathOnSubmit="/recommender"
          submitFunction={sendAnswer}
          answered={answered} 
          onNext={handleNext}
        />
      </div>
    </>
  );
}