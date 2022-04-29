import React from "react";
import { Link } from 'react-router-dom';
import { Question } from './Question';

export const Page = (props) => {

    const displayIfDefined = (page, component) => (page === undefined ? <></> : component);

    const linkToPreviousPage  = (
        <Link to={ `/page${props.prevPage }`}>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">prev</button>
        </Link>
    );

    const linkToNextPage  = (
        <Link to={ `/page${props.nextPage}` }>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">next</button>
        </Link>
    );


    return (
        <div className='grid place-items-center'>
            {props.questions.map((text, index) => 
                <Question text={text} questionNumber={index} key={index}/>
            )}
            <div className="flex">
                { displayIfDefined(props.prevPage, linkToPreviousPage) }
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">submit</button>
                { displayIfDefined(props.nextPage, linkToNextPage) }
            </div>
        </div>
    );
}