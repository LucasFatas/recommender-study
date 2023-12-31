import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ConsentPage } from "../ConsentPage";
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';

afterEach(cleanup);

it('Check if button is dissabled when a new page is loaded', () => {
    render(
        <Router>
          <ConsentPage/>
        </Router>,
    );
    expect(screen.getByRole("button",{name: /Next/i})).toBeDisabled();
});

it('Check if checkbox is not checked when a new page is loaded', () => {
    render(
        <Router>
          <ConsentPage/>
        </Router>,
    );

    const checkbox = screen.getByRole('checkbox')
    expect(checkbox).not.toBeChecked()
});

it('Check if when checkbox is ticked button is enabled', () => {
    render(
        <Router>
          <ConsentPage/>
        </Router>,
    );

    userEvent.click(screen.getByRole('checkbox'));

    expect(screen.getByRole("button",{name: /Next/i})).toBeEnabled();

})



