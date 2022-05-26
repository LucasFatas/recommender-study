import React from 'react';

export const Dashboard = () => {
  

  const logout= () => {
    console.log("log out")
  }
  const downloadSongs= () => {
    console.log("log out")
  }
  
  return (
  
    <div className='flex flex-col items-center justify-between py-28'>
      <h1> dashboard </h1>
      <div className='flex rounded-[20px] mx-10 px-5 py-6 border-solid border-4 border-gray-300 bg-gray-700' >
        <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
          <span className="text-white"> current batch </span>
        </div>
        <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
          <span className="text-white"> Download Data </span>

          {/* <div className='py-5'>
            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 rounded-full ' onClick={downloadSongs} >
              <div className='grid place-items-center '>
                <span className="text-white"> songs </span>
              </div>
            </button> 
          </div>
          <div>
            <button className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 rounded-full ' onClick={downloadSongs} >
              <div className='grid place-items-center '>
                <span className="text-white"> scores </span>
              </div>
           </button> 
          </div> */}
          


        </div>
      </div>
      <button className='text-right bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={logout} >
        <div className='grid place-items-center '>
          <span className="text-white"> log out </span>
        </div>
      </button> 
    </div>
  )
}