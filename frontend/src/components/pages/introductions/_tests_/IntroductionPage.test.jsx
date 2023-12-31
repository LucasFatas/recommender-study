import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { IntroductionPage } from '../IntroductionPage';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';


afterEach(cleanup);

it('Check if button is enabled when a new page is loaded', () => {
    render(
        <Router>
          <IntroductionPage intro={{title : "Introduction personality questionnaire", introduction : "a"}} nextpage={'/questionnaire/p/page1'} />
        </Router>,
    );
    expect(screen.getByRole("button")).toBeEnabled();
});