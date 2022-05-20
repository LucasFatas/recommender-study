import React from "react";
import { useState } from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';
import { QuestionnairePage } from './QuestionnairePage';
import { PageNotFound } from "../errors/PageNotFound";

export const Questionnaire = ({ questions, defaultPage }) => {

  const [answers, setAnswers] = useState(new Map());
    
  const questionsArray = questions.questions;
  const questionsPerPage = questions.questionsPerPage;

  /** 
   * Splits the array of questions into a 2D array where each row is an 
   * array of questions that is going to appear on one page.
   * The number of rows always equals the number of pages in the questionnaire.
   */
  const questionMatrix = questionsArray.map((e, i) => {
      return i % questionsPerPage === 0 ? questionsArray.slice(i, i + questionsPerPage).map((e, idx) => [e, i + idx]) : null;
  }).filter(e => { return e; });

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
        {
          questionMatrix.map((questions, idx) => (
            <Route path={`page${idx + 1}`} key={idx + 1} element={currentPage(questions, idx)}/>
          ))
        }
      </Routes>
    )
}