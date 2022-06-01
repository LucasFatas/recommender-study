import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Buttons } from '../Buttons';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';


afterEach(cleanup);

it('Check Submit and Previous button', () => {
    render(
        <Router>
             <Buttons 
                 prevPage={true} 
                 showSubmit={true} //boolean condition to decide whether to show submit button
                 nextPage={false} //boolean condition to decide whether to show next button
                 answered={false}  //boolean condition to decide whether to activate next button
                 onNext={{}} //function to execute everytime next button is pressed
                 data={{}} //data object, parameters are specified right below
                 pathOnSubmit={''} //path to route after submit button is pressed
                 submitFunction={{}} //function to execute on submit
                 currentPath={''} //current path of the page
                 submitResults={false} //boolean condition to decide whether to execute submit function
             />
        </Router>,
    );
    expect(screen.getByRole("button",{name: /Previous/i})).toBeEnabled();
    expect(screen.getByRole("button",{name: /Submit/i})).toBeDisabled();
});

it('Check Submit and Previous button', () => {
    render(
        <Router>
             <Buttons 
                 prevPage={true} 
                 showSubmit={false} //boolean condition to decide whether to show submit button
                 nextPage={true} //boolean condition to decide whether to show next button
                 answered={true}  //boolean condition to decide whether to activate next button
                 onNext={{}} //function to execute everytime next button is pressed
                 data={{}} //data object, parameters are specified right below
                 pathOnSubmit={''} //path to route after submit button is pressed
                 submitFunction={{}} //function to execute on submit
                 currentPath={''} //current path of the page
                 submitResults={false} //boolean condition to decide whether to execute submit function
             />
        </Router>,
    );
    expect(screen.getByRole("button",{name: /Next/i})).toBeEnabled();
});