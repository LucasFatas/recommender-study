import { Questionnaire } from './components/questionnaire/Questionnaire';
import { PageNotFound } from './components/errors/PageNotFound';
import { ErrorRouter } from './components/errors/ErrorRouter';
import { Recommender } from './components/recommender/Recommender';
import { WebsiteIntroduction } from './components/pages/introductions/WebsiteIntroduction';
import { Introduction } from './components/pages/introductions/Introduction';
import { ConsentPage } from './components/pages/ConsentPage';
import { Thanks } from './components/pages/Thanks';
import { ResultPage } from './components/pages/ResultPage';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import questions from './util/questions.json';
import * as data from './util/API.json'
import * as valueIntro from './util/valueIntroductions.json'
import * as personalityIntro from './util/personalityIntroduction.json'
import * as playlistIntro from './util/playlistIntroduction.json'

const App = () => {

  const defaultPage = '/loginPage';

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to={defaultPage}/>} />
        <Route path="/error/*" element={<ErrorRouter defaultPage={defaultPage} />} />
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>

        <Route path="/websiteIntroduction" element={<WebsiteIntroduction data={data}/>} />
        <Route path="/valuesIntroduction" element={<Introduction intro={valueIntro} nextpage={'/questionnaire'} />} />
        <Route path="/personalityIntroduction" element={<Introduction intro={personalityIntro} nextpage={'/questionnaire'} />} />
        <Route path="/playlistIntroduction" element={<Introduction intro={playlistIntro} nextpage={'/recommender'} />} />
        <Route path="/consentPage"  element={<ConsentPage defaultPage={defaultPage}/>} />
        <Route path="/questionnaire/*" element={<Questionnaire questions={questions} defaultPage={defaultPage} />} />
        <Route path="/recommender" element={<Recommender/>} />
        <Route path="/resultPage" element={<ResultPage/>} />
        <Route path="/thanks" element={<Thanks/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;