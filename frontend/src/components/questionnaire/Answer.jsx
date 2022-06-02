import React from "react";

import { RadioButton } from "../global/RadioButton";

export const Answer = (props) => {

  const {
    optionsPerAnswer,
    type
  } = props;

  const inputs = [];

  for (let i = 1; i <= optionsPerAnswer; i++)
    inputs.push(<RadioButton {...props} key={i} value={i} />)

  return (
    <div className="flex justify-center w-fit mt-5 space-x-7 ">
      {type === 'values'
        ? ""
        : <h3 className="">Disagree</h3>
      }
      {inputs}
      {type === 'values'
        ? ""
        : <h3 className="">Agree</h3>
      }
    </div>
  )
}