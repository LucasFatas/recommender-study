import { Question } from './components/Question';
import { Buttons } from './components/Buttons';



const App = () => {

  const questions = [
    'What is your name?',
    'How old are you?',
    'Where are you from?'
  ]

  return (
    <div className='grid place-items-center'>
      {questions.map((text, index) => 
        <Question text={text} questionNumber={index}/>
      )}

      <Buttons/>
    </div>
  );
}

export default App;