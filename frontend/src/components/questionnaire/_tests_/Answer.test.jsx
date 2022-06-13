import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Answer } from '../Answer';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';

afterEach(cleanup);


let x = 0;

it('Check if button is enabled when a new page is loaded', () => {
    render(
        <Router>
          <Answer 
             optionsPerAnswer={5}
             answers={new Map()} //Map containing questionnaire answers
             value={1} //Number : Value of the current radio button (if it's the first it'll be 1 and so on...)
             questionNumber={1} //Number : question number
             onChange={() => x++}
             type={'values'} //?String, can be either 'personality', 'values' or undefined.
          />
        </Router>,
    );
    const lst = screen.getAllByRole('radio');
    for(let x =0; x < lst.length; x++){
      expect(lst[x]).toBeEnabled();
      expect(lst[x]).not.toBeChecked();
    }

    const button1 = screen.getByDisplayValue('1');
    const button2 = screen.getByDisplayValue('2');

    userEvent.click(button1);
    expect(button1).toBeChecked();
    expect(button2).not.toBeChecked();

    userEvent.click(button2);
    expect(button2).toBeChecked();
    expect(button1).not.toBeChecked();

    expect(x).toBe(2);
});
