import React from "react";
import { useState } from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';

import questions from '../../util/questions.json';
import { QuestionnairePage } from './QuestionnairePage';
import { PageNotFound } from "../errors/PageNotFound";
import { 
  splitArrayIntoMatrix, 
  loadAnswersFromStorage,
  getRandomQuestionnaire
} from "../../controller/questionnaireController";


const options = ['values', 'personality'];


//Choose which questionnaire should be shown first.
const firstQuestionnaire = getRandomQuestionnaire(options);

export const Questionnaire = (props) => {

  console.log(firstQuestionnaire);
  const sessionAnswers = sessionStorage.getItem("answers");

  const {
    defaultPage
  } = props;

  const [answers, setAnswers] = useState(
    sessionAnswers === null
    ? {
      "personality" : new Map(), 
      "values" : new Map()
    } 
    : loadAnswersFromStorage(sessionAnswers)
  );
  
  const personalityObj = questions.personality;
  const valuesObj = questions.values;
  const questionsPerPage = questions.questionsPerPage;

  const personalityQuestionsMatrix = splitArrayIntoMatrix(personalityObj.questions, questionsPerPage);
  const valuesQuestionsMatrix = splitArrayIntoMatrix(valuesObj.questions, questionsPerPage);

  const values = {
    ...valuesObj,
    matrix : valuesQuestionsMatrix,
    pathOnSubmit : firstQuestionnaire === 'values' ? '/introduction/personality' : '/recommender',
    lastPage : valuesQuestionsMatrix.length,
    path : "/v",
    type : 'values',
    submitResults : firstQuestionnaire === 'personality'
  }

  const personality = {
    ...personalityObj,
    matrix : personalityQuestionsMatrix,
    pathOnSubmit : firstQuestionnaire === 'personality' ? '/introduction/values' : '/recommender',
    lastPage : personalityQuestionsMatrix.length,
    path : "/p",
    type : 'personality',
    submitResults : firstQuestionnaire === 'values'
  }

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

  const initialPath = firstQuestionnaire === 'values' ? 'v' : 'p';

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