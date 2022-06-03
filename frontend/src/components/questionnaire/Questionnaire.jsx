import React from "react";
import { useState } from 'react';
import { Route, Routes, Navigate, useLocation } from 'react-router-dom';

import questions from '../../util/questions.json';
import { QuestionnairePage } from './QuestionnairePage';
import { PageNotFound } from "../errors/PageNotFound";
import { 
  splitArrayIntoMatrix, 
  parseSessionObj,
  getRandomQuestionnaire,
  getLastPage,
  getDataObj,
  getAndStoreUserId
} from "../../controller/questionnaireController";


const options = ['values', 'personality'];

//Choose which questionnaire should be shown first.
const firstQuestionnaire = getRandomQuestionnaire(options);

export const Questionnaire = (props) => {
  
  const {
    defaultPage,
    currentBatch
  } = props;

  const search = useLocation().search;
  if (sessionStorage.getItem("userID") === null)
    getAndStoreUserId(search);

  const sessionAnswers = sessionStorage.getItem("answers");

  const [answers, setAnswers] = useState(
    sessionAnswers === null
      ? {
        "personality" : new Map(), 
        "values" : new Map()
      } 
      : parseSessionObj(JSON.parse(sessionAnswers))
  );
  
  const initialPath = firstQuestionnaire === 'values' ? 'v' : 'p';
  const lastPage = getLastPage(currentBatch);

  const valuesObj = questions.values;
  const personalityObj = questions.personality;
  const questionsPerPage = questions.questionsPerPage;

  const personalityQuestionsMatrix = splitArrayIntoMatrix(personalityObj.questions, questionsPerPage);
  const valuesQuestionsMatrix = splitArrayIntoMatrix(valuesObj.questions, questionsPerPage);

  const values = getDataObj(valuesObj, valuesQuestionsMatrix, 'values', lastPage, firstQuestionnaire);
  const personality = getDataObj(personalityObj, personalityQuestionsMatrix, 'personality', lastPage, firstQuestionnaire);

  const questionnaireArray = firstQuestionnaire === 'values' ? [values, personality] : [personality, values];

  const currentPage = (obj, idx, questions) => {
    idx += 1;
    
    return (<QuestionnairePage
      answers={answers}
      setAnswers={setAnswers}
      submitResults={obj.submitResults}
      type={obj.type} 
      numberOfPages={obj.lastPage}
      questions={questions} 
      pageNumber={idx}
      nextIntro={obj.nextIntro}
      currentPath={obj.path}
      pathOnSubmit={obj.pathOnSubmit}
      optionsPerAnswer={obj.answerOptions}
      prevPage={idx === 1 ? false : idx - 1} 
      nextPage={idx === obj.lastPage ? false : idx + 1}
      showSubmit={idx === obj.lastPage ? obj.lastPage : false}
    />)
  }

  return (
    <Routes>
      <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
      <Route path="/" element={<Navigate replace to={`${initialPath}/page1`}/>} />
      {questionnaireArray.map(obj => 
        obj.matrix.map((questions, idx) => 
          <Route
            path={`${obj.path}/page${idx + 1}`}
            key={`${obj.path}${idx}`}
            element={currentPage(obj, idx, questions)}
          />
        )
      )}
    </Routes>
  )
}