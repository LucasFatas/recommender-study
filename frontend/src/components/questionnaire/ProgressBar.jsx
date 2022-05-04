import React from 'react';


export const ProgressBar = (props) => {
    const progressPercentage = props.pageNumber / props.numberOfPages * 100
    return (
        <div className=' sticky z-50 top-0  h-5 w-full bg-gray-300'>
            <div
                style={{ width: `${progressPercentage}%`}}
                className='h-full rounded-r-lg bg-green-600'>
            </div>
        </div>
            );
}