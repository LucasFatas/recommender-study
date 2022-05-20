import { Questionnaire } from './components/questionnaire/Questionnaire';
import { PageNotFound } from './components/errors/PageNotFound';
import { ErrorRouter } from './components/errors/ErrorRouter';
import { Recommender } from './components/recommender/Recommender';
import { Thanks } from './components/Thanks';
import { ResultPage } from './components/ResultPage';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';
import { LoginPage } from './components/LoginPage';
import * as data from './util/API.json'

const App = () => {

  const defaultPage = '/loginPage';

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to={defaultPage}/>} />
        <Route path="/error/*" element={<ErrorRouter defaultPage={defaultPage} />} />
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>


        <Route path="/loginPage"  element={<LoginPage data={data} defaultPage={defaultPage}/>} />
        <Route path="/questionnaire/*" element={<Questionnaire questions={questions} defaultPage={defaultPage} />} />
        <Route path="/recommender" element={<Recommender/>} />
        <Route path="/resultPage" element={<ResultPage/>} />
        <Route path="/thanks" element={<Thanks/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;