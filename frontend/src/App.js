import { Page } from './components/Page';
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
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
    'How much do you relate to this?',
    'Do you believe that you exist?',
    'Do you believe in the existence of god?'
  ]

  const questions3 = [
    'Bla bla bla question?',
    'words words words question?',
    'sentence sentence question?'
  ]

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate replace to="/page0"/>} />
        {/* Page 0 */}
        <Route path="/page0" element={ 
          <Page questions={questions} nextPage={1}/>
        }/>
        {/* Page 1 */}
        <Route path="/page1" element={
          <Page questions={questions2} prevPage={0} nextPage={2} />
        } />
        {/* Page 2 */}
        <Route path="/page2" element={
          <Page questions={questions3} prevPage={1} />
        } />
      </Routes>
    </BrowserRouter>
  );
}

export default App;