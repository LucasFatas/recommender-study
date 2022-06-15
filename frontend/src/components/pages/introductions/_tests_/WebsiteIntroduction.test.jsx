import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { WebsiteIntroduction } from '../WebsiteIntroduction'; 
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';

afterEach(cleanup);

it('Check if button is enabled when a new page is loaded', () => {
    render(
        <Router>
          <WebsiteIntroduction data={{serverUrl: "http://localhost",port : 5000}}/>
        </Router>,
    );
    expect(screen.getByRole("button")).toBeEnabled();
});





