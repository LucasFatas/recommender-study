import React from "react";

import { RadioButton } from "../global/RadioButton";

const optionsPerAnswer = 5;

export const Answer = (props) => {

  const {
    answers, //Map containing questionnaire answers
    onAnswerChange, //Function triggered when an answer i changed
    playlistName, //String with playlist name
    questionNumber //Number with current question number
  } = props;

  const inputs = [];

  for (let i = 1; i <= optionsPerAnswer; i++)
    inputs.push(
      <RadioButton
        answers={answers} 
        value={i}
        onChange={onAnswerChange} 
        key={i + playlistName}
        questionNumber={questionNumber}
      />);

  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      <h3 className="">Strongly disagree</h3>
      {inputs}
      <h3 className="">Strongly agree</h3>
    </div>
  )
}