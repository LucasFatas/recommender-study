import React from "react";

import { optionsPerAnswer } from "../../controller/recommenderController";
import { RadioButton } from "../global/RadioButton";

export const Feedback = (props) => {

  const questions = [];
  const currentFeedback = props.feedback[props.playlistName];

  const onAnswerChange = (e, setSelected, questionNumber, value) => {

    const questionsMap = currentFeedback.questions;
    const elementValue = e.target.value;
    const currentNumber = questionNumber + 1;

    setSelected(questionsMap.get(currentNumber) === value);
    
    questionsMap.set(currentNumber, parseInt(elementValue));
    console.log(props.feedback);
    props.setFeedback(props.feedback);
  }


  props.questions.forEach((e, i) => {

    const inputs = [];
    const currentAnswer = currentFeedback.questions[i];

    for (let j = 1; j <= optionsPerAnswer; j++)
      inputs.push(
        <RadioButton 
          value={j} 
          name={i}
          onChange={onAnswerChange} 
          key={j}
          questionNumber={i}
          answers={currentFeedback.questions}
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
      {questions}
      <textarea 
        className=' rounded-[2px] my-5 mt-10 border-4 border-green-500 resize-none' 
      
        placeholder="type your feedback" 
        maxLength="80" 
        cols="50" 
        rows="5"
        wrap="hard"
        onChange={(e) => { 
          currentFeedback.comment = e.target.value;
          props.setFeedback({...props.feedback, [props.playlistName] : { ...currentFeedback}});
        }}
        />
    </div>
  )
}