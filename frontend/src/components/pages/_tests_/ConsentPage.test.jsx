
import renderer from "react-test-renderer";
import {cleanup, screen, fireEvent, render} from '@testing-library/react';
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
    //expect(screen.getByRole('checkbox', {name: /I accept the terms and agreements./i}));
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



