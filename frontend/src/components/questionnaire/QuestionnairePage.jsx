import React from "react";
import { useState, useEffect, useMemo } from "react";

import { Answer } from './Answer';
import { Buttons } from "../global/Buttons";
import { ProgressBar } from "./ProgressBar";
import { 
  updateAnswersLogic, 
  checkEveryElementIsInMap
} from "../../controller/questionnaireController";
import { useNavigate } from "react-router-dom";
import { questionnairePageSecurity } from "../../controller/pathSecurityController";

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
    answers,
    setAnswers,
    type,
    numberOfPages,
    questions,
    pageNumber,
    pathOnSubmit,
    optionsPerAnswer,
    currentPath
  } = props;

  const navigate = useNavigate()

  useEffect(() => {
    questionnairePageSecurity(navigate, type, pageNumber)

  }, []);

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
    
    
      sessionStorage.setItem("currentUrl", "/questionnaire/" + (type === 'values' ? 'v' : 'p') + "/page" + (pageNumber + 1) )

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
      <div className="absolute text-2xl text-right p-10 text-green-600 top-0 right-0">
        <h2 className="">{pageNumber} / {numberOfPages}</h2>
      </div>
      <div className='grid place-items-center'>
        {questions.map(([text, index]) => 
          <div className='flex flex-col py-6 items-center' key={index}>
            <h1 className='text-blue-500 text-center text-[20px]'>{text}</h1>
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
          answered={answered} 
          onNext={handleNext}
        />
      </div>
    </>
  );
}