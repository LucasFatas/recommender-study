import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Introduction } from '../Introduction';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';


afterEach(cleanup);

it('Check if button is enabled when a new page is loaded', () => {
    render(
        <Router>
          <Introduction intro={{title : "Introduction personality questionnaire", introduction : "a"}} nextpage={'/questionnaire/p/page1'} />
        </Router>,
    );
    expect(screen.getByRole("button")).toBeEnabled();
});