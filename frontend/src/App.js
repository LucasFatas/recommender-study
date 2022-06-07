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
import { Dashboard } from './components/dashboard/Dashboard';
import { QuestionnaireResult } from './components/result/QuestionnaireResult';

import { LogIn } from './components/dashboard/LogIn';

import * as data from './util/API.json'
import intro from './util/introductions.json'


const defaultPage = '/consentPage';

const App = () => {


  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to={defaultPage}/>} />
        <Route path="/error/*" element={<ErrorRouter defaultPage={defaultPage} />} />
        <Route path="*" element={<PageNotFound redirect={defaultPage} />}/>

        <Route path="/login" element={<LogIn />} />
        <Route path="/dashboard" element={<Dashboard/>} />
        <Route path="/websiteIntroduction" element={<WebsiteIntroduction data={data}/>} />
        <Route path="/introduction/values" element={<Introduction intro={intro.values} nextpage="/questionnaire/v/page1" />} />
        <Route path="/introduction/personality" element={<Introduction intro={intro.personality} nextpage={'/questionnaire/p/page1'} />} />
        <Route path="/introduction/playlist" element={<Introduction intro={intro.playlist} nextpage={'/recommender'} />} />
        <Route path="/consentPage"  element={<ConsentPage defaultPage={defaultPage}/>} />
        <Route path="/questionnaire/*" element={<Questionnaire defaultPage={defaultPage} />} />
        <Route path="/results" element={<QuestionnaireResult currentBatch={currentBatch}/>} />
        <Route path="/recommender/*" element={<Recommender  defaultPage={defaultPage}/>} />
        <Route path="/resultPage" element={<ResultPage/>} />
        <Route path="/thanks" element={<Thanks/>} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;