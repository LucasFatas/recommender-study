import React from 'react';

import { getProgressPercentage } from '../../controller/questionnaireController';

export const ProgressBar = (props) => {

  const progressPercentage = getProgressPercentage(props.pageNumber, props.numberOfPages);

  return (
    <div className=' sticky z-50 top-0  h-5 w-full bg-gray-300'>
      <div
        style={{ width: `${progressPercentage}%`}}
        className='h-full rounded-r-lg bg-green-600'
      />
    </div>
  )
}