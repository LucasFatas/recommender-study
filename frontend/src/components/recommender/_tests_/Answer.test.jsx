import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Answer } from '../../recommender/Answer';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';

afterEach(cleanup);


let x = 0;

it('Check if button is enabled when a new page is loaded', () => {
    render(
        <Router>
          <Answer 
             answers={new Map()} //Map containing questionnaire answers
             onAnswerChange={() => x++} //Function triggered when an answer i changed
             playlistName={'George'} //String with playlist name
             questionNumber={1} //Number : question number
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
