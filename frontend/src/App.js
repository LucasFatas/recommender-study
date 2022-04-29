import { Page } from './components/Page';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";


const App = () => {

  /*
    When receiving all the questions split them in arrrays of 
    questions : 
    const chunkSize = 3;

    const [q1, q2, q3, q4] = arr.map((e, i) => { 
        return i % chunkSize === 0 ? arr.slice(i, i + chunkSize) : null; 
    }).filter(e => { return e; });

  */

  const questions = [
    'What is your name?',
    'How old are you?',
    'Where are you from?'
  ]

  const questions2 = [
    'What is your name?',
    'How old are you?',
    'Where are you from?'
  ]

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Page questions={questions}/>}/>
        <Route path="/page1" element={<Page questions={questions2}/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;