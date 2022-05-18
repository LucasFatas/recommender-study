import React from "react";
import { Link } from "react-router-dom";

export const PageNotFound = (props) => {

  return (
    <div className="h-3/4 w-screen flex flex-col justify-center content-center items-center absolute z-0">
      <h1 className="uppercase p-10 text-xl font-black">
        We're sorry, but something went wrong.
      </h1>
      <Link to={props.redirect}>
        <button className="bg-blue-500 hover:bg-blue-700 text-lg text-white font-bold py-2 px-4 rounded-full ">
          Back to homepage
        </button>
      </Link>
    </div>
  )
}