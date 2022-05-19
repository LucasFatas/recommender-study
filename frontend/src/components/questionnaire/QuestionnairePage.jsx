import React from "react";
import { useState, useEffect, useMemo } from "react";

import { Answer } from './Answer';
import { Buttons } from "../global/Buttons";
import { ProgressBar } from "./ProgressBar";
import { sendAnswer } from '../../API/Questionnaire';

export const QuestionnairePage = (props) => {
  
  //boolean value to check if all answers in the current page have been answered.
  const [ answered, setAnswered ] = useState(false);
  const questionsNumber = useMemo(() => [...props.questions.map(x => x[1] + 1)], [props.questions]);
  
  useEffect(() => 
    setAnswered(questionsNumber.every(x => props.answers.has(x))),
    [questionsNumber, props.answers] //parameters that, if changed, trigger the function above
  );

  const updateAnswers = (e, setSelected, questionNumber, value) => {
    //Set solution in answers map
    props.setAnswers(props.answers.set(questionNumber + 1, parseInt(e.target.value)));
    
    //Set selected radio button in answer
    setSelected(props.answers.get(questionNumber + 1) === value);
    
    //Change boolean value
    setAnswered(questionsNumber.every(x => props.answers.has(x)));
  }

  const handleNext = () => {
    const nextQuestionsNumber = questionsNumber.map(x => x + questionsNumber.length);
    setAnswered(nextQuestionsNumber.every(x => props.answers.has(x)))
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