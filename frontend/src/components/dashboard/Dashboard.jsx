import React, { useState } from 'react';

export const Dashboard = () => {
  
  // const inputStyle = "appearance-none rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer";
  const batchNumber = 1
  const batchUsers = 1
  const batchMetric = "euclidian"
  const batchType = "Questionnaire"

  const downloadData = ["Songs", "Q&A", "Rating&Feedback", "Scores"]
  const batchs = [1,2]

  const logout= () => {
    console.log("log out")
  }
  const downloadCSV= () => {
    console.log("download CSV")
    
    console.log(batchToDownload, dataToDownload)
  }

  const [dataToDownload, setDataToDownload] = useState("");
  const [batchToDownload, setBatchToDownload] = useState("");
  
  return (
  
    <div className='flex flex-col items-center justify-between py-28'>
      <div className='flex rounded-[20px] mx-10 px-5 py-6 border-solid border-4 border-gray-300 bg-gray-700' >
        <div className='flex flex-col'>
          <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
            <span className="text-white text-center text-xl"> Current Batch </span>
            <div className='flex'>
              <span className="text-white pr-3"> Batch #: </span>
              <span className="text-white pr-3"> {batchNumber} </span>
            </div>
            <div className='flex'>
              <span className="text-white pr-3"> Number of users: </span>
              <span className="text-white pr-3"> {batchUsers} </span>
            </div>
            <div className='flex'>
              <span className="text-white pr-3"> Type of batch: </span>
              <span className="text-white pr-3"> {batchType} </span>
            </div>
            <div className='flex'>
              <span className="text-white pr-3"> Metric: </span>
              <span className="text-white pr-3"> {batchMetric} </span>
            </div>
          </div>
          <div className='py-2 text-center'>
            <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={logout} >
              <div className='grid place-items-center '>
                <span className="text-white"> New Batch </span>
             </div>
           </button> 
          </div>
        </div>
        
        <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
          <span className="text-white text-center text-xl"> Download Data </span>
          <div className='flex'>
            <span className="text-white pr-3"> Data: </span>
            {downloadData.map((data, index) => 
              (<div className='pr-3 '>
                <input 
                  type="radio" 
                  // className={inputStyle} 
                  value={data}
                  name={"data"}
                  onChange={e => setDataToDownload(e.target.value)}
                /> 
                <span className="text-white"> {data} </span>
              </div>)
            )}
            
          </div>
          <div className='flex'>
            <span className="text-white pr-3"> Batch: </span>
            {batchs.map((batch, index) => 
              (<div className='pr-3 '>
                <input 
                  type="radio" 
                  // className={inputStyle} 
                  value={batch}
                  name={"batch"}
                  onChange={e => setBatchToDownload(e.target.value)}
                /> 
                <span className="text-white"> {batch} </span>
              </div>)
            )}
            
          </div>

          <div className='text-center '>
            <form method="get" action="file.doc">
              <button type="submit" className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-2 rounded-full ' onClick={downloadCSV} >
                <div className='grid place-items-center align-text-bottom'>
                  <span className="text-white"> Download </span>
                </div>
              </button> 
            </form>
          </div>
        </div>
        
      </div>
      <div className='py-2'>
        <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={logout} >
          <div className='grid place-items-center '>
            <span className="text-white"> log out </span>
          </div>
        </button> 
      </div>
      
    </div>
  )
}