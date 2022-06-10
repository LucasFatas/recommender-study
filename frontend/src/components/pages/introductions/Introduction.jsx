import React from "react";
import { Routes, Route, useLocation, Navigate } from "react-router-dom";

import { IntroductionPage } from "./IntroductionPage";
import { getAndStoreUserId, getRandomQuestionnaire } from "../../../controller/questionnaireController";

const options = ['values', 'personality'];
const firstQuestionnaire = getRandomQuestionnaire(options);

export const Introduction = (props) => {

  const { intro } = props;

  console.log(firstQuestionnaire);

  const search = useLocation().search;
  if (sessionStorage.getItem("userID") === null)
    getAndStoreUserId(search);

  return (
    <Routes>
      <Route path="/" element={<Navigate replace to={firstQuestionnaire}/>}/>
      <Route path="values" element={<IntroductionPage intro={intro.values} nextpage="/questionnaire/v/page1" />} />
      <Route path="personality" element={<IntroductionPage intro={intro.personality} nextpage={'/questionnaire/p/page1'} />} />
      <Route path="playlist" element={<IntroductionPage intro={intro.playlist} nextpage={'/recommender'} />} />
    </Routes>
  )

}