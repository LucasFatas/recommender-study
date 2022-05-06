import { QuestionnairePage } from './components/questionnaire/QuestionnairePage';
import { PageNotFound } from './components/PageNotFound';
import { ErrorPage } from './components/ErrorPage';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';
import { useState } from 'react';
import { LoginPage } from './components/LoginPage';

const App = () => {

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
  
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to="/pageLogin"/>} />
        <Route path="/pageLogin" element={<LoginPage/>} />
        <Route path="/error/database"  element={<ErrorPage redirectPath="/page1"/>} />
        <Route path="/error/login"  element={<ErrorPage redirectPath="/page1"/>} />
        {
  
          questionMatrix.map((questions, idx) => (
            <Route path={`/page${idx + 1}`} key={idx + 1} element={
              <QuestionnairePage
                answers={answers} 
                setAnswers={setAnswers}
                numberOgPages={lastPageIdx}
                questions={questions} 
                pageNumber={idx + 1}
                prevPage={idx + 1 === 1 ? false : idx} 
                nextPage={idx + 1 === lastPageIdx ? false : idx + 2}
                showSubmit={idx + 1 === lastPageIdx ? lastPageIdx : false}
              />
            }/>
          ))
        }

        <Route path="*" element={<PageNotFound redirectPath="/page1"/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;