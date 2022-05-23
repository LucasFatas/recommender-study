import React from "react";

import { handleComment } from "../../controller/recommenderController";
import { Answer } from "./Answer";

export const Feedback = (props) => {

  const {
    feedback,
    playlistName,
    questions,
    setFeedback
  } = props;

  const currentFeedback = feedback[playlistName];

  return (
    <div className="flex flex-col items-center content-center">
      {questions.map((e, i) => (
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
        value={currentFeedback.comment}
        name={playlistName}
        onChange={e => handleComment(e, currentFeedback, feedback, setFeedback, playlistName)}
      />
    </div>
  )
}