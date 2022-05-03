import React from "react";
import { Question } from './Question';
import { Buttons } from "./Buttons";


export const Page = (props) => {
    const progressPercentage = 70
    return (

        <>
            <div className=' relative grid place-items-center'></div>
                <div className=' sticky z-50 top-0  h-5 w-full bg-gray-300'>
                    <div
                        style={{ width: `${progressPercentage}%`}}
                        className='h-full rounded-r-lg bg-green-600'>
                    </div>
                </div>
            <div/>
            <div className='grid place-items-center'>
                
                
                
                {props.questions.map(([text, index]) => 
                    <Question text={text} questionNumber={index} key={index}/>
                )}
                <Buttons {...props} />
            </div>
        </>
    );
}