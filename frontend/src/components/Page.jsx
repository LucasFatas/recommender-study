import React from "react";
import { Question } from './Question';
import { Buttons } from "./Buttons";

export const Page = (props) => {
    return (
        <div className='grid place-items-center'>
            {props.questions.map(([text, index]) => 
                <Question text={text} questionNumber={index} key={index}/>
            )}
            <Buttons {...props} />
        </div>
    );
}