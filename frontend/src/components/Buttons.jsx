import { useState } from 'react';
import { Link } from 'react-router-dom';

const buttonStyle = "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ";
const buttonStyleDisabled = " select-none text-transparent fonted bg-transparent hover:bg-transparent  py-2 px-4 rounded-full ";


export const Buttons = (props) => {

    const setStyleAndDisabled = (cond) => {
        return { 
            className : cond === undefined ? buttonStyleDisabled : buttonStyle,
            disabled : cond === undefined ? true : false
        }
    }
    
    return (
        <div className="flex justify-center w-fit mt-5 space-x-7 ">
            <Link to={ `/page${props.prevPage }`}>
                <button {...setStyleAndDisabled(props.prevPage)}>
                    Previous
                </button> 
            </Link>
            <button {...setStyleAndDisabled(props.showSubmit)}>
                Submit
            </button>
            <Link to={ `/page${props.nextPage }` }>
                <button {...setStyleAndDisabled(props.nextPage)}>
                    Next
                </button>
            </Link>
        </div>
    );
}