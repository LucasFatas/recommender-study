import React from "react";

const inputStyle = "appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer";
const optionsPerAnswer = 5;

export const Feedback = (props) => {

  const questions = [];

  props.questions.forEach((e, i) => {

    const inputs = [];

    for (let j = 1; j <= optionsPerAnswer; j++)
      inputs.push(<input type="radio" className={inputStyle} value={j} name={i} key={j}/>)

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
        rows="10"
        wrap="hard"
        onChange={(e) => { 
          props.comment.playlistName = e.target.value;
          props.setComment(props.comment);
        }}
        />
    </div>
  )
}