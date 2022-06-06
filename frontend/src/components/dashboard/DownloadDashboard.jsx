import React from 'react';
import { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';
import { isLoggedIn, retrieveCSV } from "../../controller/dashboardController";
import { CSVLink} from 'react-csv'

export const DownloadDashboard = ({downloadData, setDataToDownload, setBatchToDownload, batchs, canDownload, CSVToDownload, batchToDownload, dataToDownload, setCSVToDownload, setCanDownload, date}) => {

  return (
    <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
    <span className="text-white text-center text-xl"> Download Data </span>
    <div className='flex'>
      <span className="text-white pr-3"> Data: </span>
      {downloadData.map((data, index) => 
        (<div key={index} className='pr-3 '>
          <input 
            type="radio" 
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
        (<div key={index} className='pr-3 '>
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

    <div className='text-center py-5'>
        <button type="submit" className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-2 rounded-full ' onClick={() => retrieveCSV(batchToDownload, dataToDownload, setCSVToDownload, setCanDownload)} >
          <div className='grid place-items-center align-text-bottom'>
            <span className="text-white"> Retrieve Data </span>
          </div>
        </button> 
    </div>
    {
      canDownload
      ?
        <div className='text-center'>
          <CSVLink
            data={CSVToDownload}
            separator={","}
            enclosingCharacter={`"`}
            filename={dataToDownload + " "+ date() + ".csv"}
          >
            <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full '  onClick={() => setCanDownload(false)}>
              <div className='grid place-items-center '>
                <span className="text-white"> download </span>
              </div>
            </button> 
          </CSVLink>
        </div>
      :
        <></>
    }
    
  </div>
  )
}
