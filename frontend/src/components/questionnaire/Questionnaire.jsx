import React from "react";
import { useState } from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';
import { QuestionnairePage } from './QuestionnairePage';
import { PageNotFound } from "../errors/PageNotFound";
import { splitArrayIntoMatrix } from "../../controller/questionnaireController";

export const Questionnaire = ({ questions, defaultPage }) => {

  const [answers, setAnswers] = useState(new Map());
    
  const questionsArray = questions.questions;
  const questionsPerPage = questions.questionsPerPage;

  const questionMatrix = splitArrayIntoMatrix(questionsArray, questionsPerPage);

  const lastPageIdx = questionMatrix.length;

  const currentPage = (questions, idx) => {
    idx += 1;
    
    return (<QuestionnairePage
      answers={answers} 
      setAnswers={setAnswers}
      numberOgPages={lastPageIdx}
      questions={questions} 
      pageNumber={idx}
      prevPage={idx === 1 ? false : idx - 1} 
      nextPage={idx === lastPageIdx ? false : idx + 1}
      showSubmit={idx === lastPageIdx ? lastPageIdx : false}
    />)
  }

    return (
      <Routes>
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>
        <Route path="/" element={<Navigate replace to="page1"/>} />
        {questionMatrix.map((questions, idx) => (
          <Route path={`page${idx + 1}`} key={idx + 1} element={currentPage(questions, idx)}/>
        ))}
      </Routes>
    )
}