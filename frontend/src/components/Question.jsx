import React from 'react';

import { Answer } from './Answer';

export const Question = (props) => {

    return (
        <div className='flex flex-col py-10 items-center'>
            <h1 className='text-blue-500 text-center text-2xl'>{props.text}</h1>
            <Answer questionNumber={props.questionNumber}/>
        </div>
    );
}