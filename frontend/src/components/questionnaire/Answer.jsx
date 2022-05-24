import React from "react";

import { RadioButton } from "../global/RadioButton";
import { optionsPerAnswer } from "../../controller/questionnaireController";

export const Answer = (props) => {

  const inputs = [];

  for (let i = 1; i <= optionsPerAnswer; i++)
    inputs.push(<RadioButton {...props} key={i} value={i} />)

  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      <h3 className="">Strongly disagree</h3>
      {inputs}
      <h3 className="">Strongly agree</h3>
    </div>
  )
}