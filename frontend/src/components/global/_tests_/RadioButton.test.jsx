import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { RadioButton } from '../RadioButton';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';


afterEach(cleanup);

let x = 0;

it('Check if Radio Button is allways enabled', () => {
    render(
        <Router>
             <RadioButton 
                     answers={new Map()} //Map containing questionnaire answers
                     value={1} //Number : Value of the current radio button (if it's the first it'll be 1 and so on...)
                     questionNumber={1} //Number : question number
                     onChange={() => x++} //Function that triggers when an answer is changed
                     type={'values'} //?String, can be either 'personality', 'values' or undefined.
             />
        </Router>,
    );
    
    expect(screen.getByRole("radio")).toBeEnabled();
    const button = screen.getByRole('radio');
    expect(button).not.toBeChecked();
    userEvent.click(button);
    expect(button).toBeChecked();
    expect(x).toBe(1)
});
