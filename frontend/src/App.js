import { Questionnaire } from './components/questionnaire/Questionnaire';
import { PageNotFound } from './components/errors/PageNotFound';
import { ErrorRouter } from './components/errors/ErrorRouter';
import { Recommender } from './components/recommender/Recommender';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';
import { LoginPage } from './components/LoginPage';

const App = () => {

  const defaultPage = '/loginPage';

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to={defaultPage}/>} />
        <Route path="/error/*" element={<ErrorRouter defaultPage={defaultPage} />} />
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>


        <Route path="/loginPage" element={<LoginPage defaultPage={defaultPage}/>} />
        <Route path="/questionnaire/*" element={<Questionnaire questions={questions} defaultPage={defaultPage} />} />
        <Route path="/recommender" element={<Recommender defaultPage={defaultPage}/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;