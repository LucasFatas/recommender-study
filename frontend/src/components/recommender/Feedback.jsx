import React, { useEffect } from "react";

import { optionsPerAnswer } from "../../controller/recommenderController";
import { RadioButton } from "../global/RadioButton";
import { Answer } from "./Answer";

export const Feedback = (props) => {

  const questions = [];
  const currentFeedback = props.feedback[props.playlistName];

  const handleComment = e => {
    currentFeedback.comment = e.target.value;
    props.setFeedback({...props.feedback, [props.playlistName] : { ...currentFeedback}});
  }

  props.questions.forEach((e, i) => {

    const inputs = [];

    for (let j = 1; j <= optionsPerAnswer; j++)
      inputs.push(
        <RadioButton
          answers={props.answers} 
          value={j}
          onChange={props.onAnswerChange} 
          key={j}
          questionNumber={i}
        />);

    questions.push(
      <div key={i} className="p-8">
        <h1 className="text-center text-xl">{e}</h1>
        <div className="flex justify-center w-fit mt-5 space-x-7">
          {inputs}
        </div>
      </div>
    )
  })

  return (
    <div className="flex flex-col items-center content-center">
      {props.questions.map((e, i) => (
        <div key={i} className="p-8">
          <h1 className="text-center text-xl">{e}</h1>
          <div className="flex justify-center w-fit mt-5 space-x-7">
            <Answer {...props} questionNumber={i}/>
          </div>
        </div>
      ))}
      <textarea 
        className=' rounded-[2px] my-5 mt-10 border-4 border-green-500 resize-none' 
      
        placeholder="type your feedback" 
        maxLength="80" 
        cols="50" 
        rows="5"
        wrap="hard"
        onChange={handleComment}
        />
    </div>
  )
}