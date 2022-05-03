import { QuestionnairePage } from './components/QuestionnairePage';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';

const App = () => {

  const questionsArray = questions.questions;
  const questionsPerPage = 5

  /** Splits the array of questions into a 2D array where each row is an 
   *  array of questions that is going to appear on one page.
   *  The number of rows always equals the number of pages in the questionnaire.
   */
  const questionMatrix = questionsArray.map((e, i) => {
    return i % questionsPerPage === 0 ? questionsArray.slice(i, i + questionsPerPage).map((e, idx) => [e, i + idx]) : null;
  }).filter(e => { return e; });

  const lastPageIdx = questionMatrix.length;

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to="/page0"/>} />

        {
          questionMatrix.map((questions, idx) => (
            <Route path={`/page${idx}`} key={idx} element={
              <QuestionnairePage 
                pageNumber={idx}
                numberOgPages={lastPageIdx}
                questions={questions} 
                prevPage={idx === 0 ? undefined : idx - 1} 
                nextPage={idx === lastPageIdx - 1 ? undefined : idx + 1}
                showSubmit={idx === lastPageIdx - 1 ? lastPageIdx - 1 : undefined}
              />
            }/>
          ))
        }
      </Routes>
    </BrowserRouter>
  );
}

export default App;