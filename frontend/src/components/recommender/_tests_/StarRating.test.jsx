import {cleanup, screen, fireEvent, render} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { StarRating } from '../StarRating';
import {BrowserRouter as Router} from 'react-router-dom';
import '@testing-library/jest-dom/extend-expect';

afterEach(cleanup);


let x = 0;

it('Check stars', () => {
    render(
        <Router>
          <StarRating
            starStyle={''} //String containing CSS style of the star buttons
            playlistName={'values'} //String with playlist name, either 'random', 'personality' or 'values'
            song={0} //Number containing index of current song
            setRatings={() => x++} //Function to change ratings object
            ratings={{
                random : { playlist: 0, songs: Array(5).fill(0) },
                personality : { playlist: 0, songs: Array(5).fill(0) },
                values : { playlist: 0, songs: Array(5).fill(0) },
            }}  //Object, to see structure go to recommenderController and check initialRatingsObj
            setRatingsFilled={() => x++}  //Function to change value of boolean ratingsFilled
          />
        </Router>,
    );

    const lst = screen.getAllByRole('button');
    for(let x =0; x < lst.length; x++){
      expect(lst[x]).toBeEnabled();
      expect(lst[x]).not.toBeChecked();    
    }
});
