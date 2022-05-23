import React from "react";

import { RadioButton } from "../global/RadioButton";

const optionsPerAnswer = 5;

export const Answer = (props) => {

  const inputs = [];

  for (let i = 1; i <= optionsPerAnswer; i++)
    inputs.push(
      <RadioButton
        answers={props.answers} 
        value={i}
        onChange={props.onAnswerChange} 
        key={i}
        questionNumber={props.questionNumber}
      />);

  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      <h3 className="">Strongly disagree</h3>
      {inputs}
      <h3 className="">Strongly agree</h3>
    </div>
  )
}