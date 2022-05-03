<<<<<<< HEAD
import { Question } from './components/Question';
import { useState } from 'react';
import { useEffect } from 'react';

=======
import { Page } from './components/Page';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from "react-router-dom";
>>>>>>> react-router

import questions from './util/questions.json';

const App = () => {

<<<<<<< HEAD
  const [inputQuestions, setinputQuestions] = useState([]);


  useEffect(()=>{
    fetch('http://localhost:5000/getQuestions',{
      'methods':'GET',
      headers : {
        'Content-Type':'application/json'
      }
    })
    .then(response => response.json())
    .then(response => setinputQuestions(response))
    .catch(error => console.log(error))

  },[])

  var questions = [
    'Basic question?'
  ] 
  questions.push.apply(questions, inputQuestions)
  
=======
  const questionsList = questions.questions;

  const questionsPerPage = 5
  
  const questionMatrix = questionsList.map((e, i) => {
    return i % questionsPerPage === 0 ? questionsList.slice(i, i + questionsPerPage).map((e, idx) => [e, i + idx]) : null;
  }).filter(e => { return e; });

  const lastQuestionIdx = questionMatrix.length;
>>>>>>> react-router

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
                showSubmit={idx === lastQuestionIdx - 1 ? lastQuestionIdx - 1 : undefined}
              />
            }/>
          ))
        }
      </Routes>
    </BrowserRouter>
  );
}

export default App;