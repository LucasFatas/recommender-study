import { Page } from './components/Page';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';

const App = () => {

  const questionsList = questions.questions;

  const questionsPerPage = 5
  
  const questionMatrix = questionsList.map((e, i) => {
    return i % questionsPerPage === 0 ? questionsList.slice(i, i + questionsPerPage).map((e, idx) => [e, i + idx]) : null;
  }).filter(e => { return e; });

  const lastQuestionIdx = questionMatrix.length;

  console.log(questionMatrix);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to="/page0"/>} />

        {
          questionMatrix.map((questions, idx) => (
            <Route path={`/page${idx}`} key={idx} element={
              <Page 
                pageNumber={idx}
                questions={questions} 
                prevPage={idx === 0 ? undefined : idx - 1} 
                nextPage={idx === lastQuestionIdx - 1 ? undefined : idx + 1}
                showSubmit={idx === lastQuestionIdx - 1}
              />
            }/>
          ))
        }
      </Routes>
    </BrowserRouter>
  );
}

export default App;