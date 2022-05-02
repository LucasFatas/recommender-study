import React from 'react';

const buttonStyle = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ";
const buttonStyleDisabled = "disabled text-white fonted bg-blue-200 hover:bg-blue-400  py-2 px-4 rounded-full ";


export const Buttons = () => {

    return (
        <div className="flex justify-center w-fit mt-5 space-x-7 ">
           
            <button className={buttonStyle} onClick={() => console.log('Previous')}>
                Previous
            </button> 
            <button className={buttonStyleDisabled} disabled onClick={() => console.log('Submit')}>
                Submit
            </button>
            <button className={buttonStyle}>
                Next
            </button>
      </div>
    );
}