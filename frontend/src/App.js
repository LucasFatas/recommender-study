import { useState } from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";

import { Questionnaire } from './components/questionnaire/Questionnaire';
import { PageNotFound } from './components/errors/PageNotFound';
import { ErrorRouter } from './components/errors/ErrorRouter';
import { Recommender } from './components/recommender/Recommender';
import { WebsiteIntroduction } from './components/pages/introductions/WebsiteIntroduction';
import { Introduction } from './components/pages/introductions/Introduction';
import { ConsentPage } from './components/pages/ConsentPage';
import { Thanks } from './components/pages/Thanks';
import { ResultPage } from './components/pages/ResultPage';

import * as data from './util/API.json'
import intro from './util/introductions.json'

import { switchBatch } from './controller/dashboardController';

const defaultPage = '/loginPage';

const App = () => {

  const [currentBatch, setCurrentBatch] = useState('questionnaire');

  //Call this function to switch batch
  /* 
    TODO : once the dashboard is implemented, pass this function 
    to the Dashboard component and call it from there.
  */
  const switchCurrentBatch = () => switchBatch(currentBatch, setCurrentBatch);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to={defaultPage}/>} />
        <Route path="/error/*" element={<ErrorRouter defaultPage={defaultPage} />} />
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>

        <Route path="/websiteIntroduction" element={<WebsiteIntroduction data={data}/>} />
        <Route path="/introduction/values" element={<Introduction intro={intro.values} nextpage="/questionnaire/v/page1" />} />
        <Route path="/introduction/personality" element={<Introduction intro={intro.personality} nextpage={'/questionnaire/p/page1'} />} />
        <Route path="/introduction/playlist" element={<Introduction intro={intro.playlist} nextpage={'/recommender'} />} />
        <Route path="/consentPage"  element={<ConsentPage defaultPage={defaultPage}/>} />
        <Route path="/questionnaire/*" element={<Questionnaire defaultPage={defaultPage} currentBatch={currentBatch}/>} />
        <Route path="/recommender/*" element={<Recommender  defaultPage={defaultPage}/>} />
        <Route path="/resultPage" element={<ResultPage/>} />
        <Route path="/thanks" element={<Thanks/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;