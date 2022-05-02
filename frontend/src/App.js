import { Question } from './components/Question';
import { useState } from 'react';
import { useEffect } from 'react';



const App = () => {

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
  

  return (
    <div className='grid place-items-center'>
      {questions.map((text, index) => 
        <Question text={text} questionNumber={index}/>
      )}
    </div>
  );
}

export default App;