import React from "react";

export const Answer = (props) => {


    return (
      <div className="flex w-fit mt-5 child:mx-1 ">
        <h3 className="pr-10">Strongly disagree</h3>
        <input className="w-10" type="radio" value="1" name={props.questionNumber} /> 
        <input className="w-10" type="radio" value="2" name={props.questionNumber} /> 
        <input className="w-10" type="radio" value="3" name={props.questionNumber} checked/> 
        <input className="w-10" type="radio" value="4" name={props.questionNumber} /> 
        <input className="w-10" type="radio" value="5" name={props.questionNumber} /> 
        <h3 className="pl-10">Strongly agree</h3>
      </div>
    )
}