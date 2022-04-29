import React from "react";

export const Answer = (props) => {

    const inputStyle = "appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer";

    return (
      <div className="flex justify-center w-fit mt-5 space-x-7 ">
        <h3 className="">Strongly disagree</h3>
        <input className={inputStyle} type="radio" value="1" name={props.questionNumber} /> 
        <input className={inputStyle} type="radio" value="2" name={props.questionNumber} /> 
        <input className={inputStyle} type="radio" value="3" name={props.questionNumber} /> 
        <input className={inputStyle} type="radio" value="4" name={props.questionNumber} /> 
        <input className={inputStyle} type="radio" value="5" name={props.questionNumber} /> 
        <h3 className="">Strongly agree</h3>
      </div>
    )
}