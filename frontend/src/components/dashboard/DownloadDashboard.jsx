import React from 'react';
import { retrieveCSV } from "../../controller/dashboardController";
import { CSVLink} from 'react-csv'

export const DownloadDashboard = ({downloadData, setDataToDownload, setBatchToDownload, batchs, canDownload, CSVToDownload, batchToDownload, dataToDownload, setCSVToDownload, setCanDownload, date}) => {

  return (
    <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
    <span className="text-white text-center text-2xl"> Download Data </span>
    <span className="text-white text-xl py-4"> Data: </span>
    <div className='grid grid-cols-3 grid-rows-2'>
      {downloadData.map((data, index) => 
        (<div key={index} className='flex items-center'>
          <input 
            type="radio" 
            value={data}
            name={"data"}
            onChange={e => setDataToDownload(e.target.value)}
          /> 
          <span className="text-white ml-5"> {data} </span>
        </div>)
      )}
    </div>
    <div className='flex py-8'>
      <span className="text-white text-xl pr-8"> Batch: </span>
      <div className='flex justify-center items-center'>
      {batchs.map((batch, index) => 
        (<div key={index} className='pr-8 flex justify-center'>
          <input 
            type="radio" 
            // className={inputStyle} 
            value={batch}
            name={"batch"}
            onChange={e => setBatchToDownload(e.target.value)}
            /> 
          <span className="text-white pl-2">{batch}</span>
        </div>)
      )}  
    </div>
    </div>
  
    <div className='flex flex-col items-center justify-center'>
      <button type="submit" className='py-2 bg-blue-500 hover:bg-blue-700 text-white font-bold w-1/3 rounded-full' onClick={() => retrieveCSV(batchToDownload, dataToDownload, setCSVToDownload, setCanDownload)} >
        Retrieve Data
      </button>
      {
        canDownload
        ?
        <CSVLink
          data={CSVToDownload}
          separator={","}
          enclosingCharacter={`"`}
          filename={dataToDownload + date() + ".csv"}
        >
          <button className='mt-6 py-2 px-4 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-full'  onClick={() => setCanDownload(false)}>
              Download 
          </button> 
        </CSVLink>
        : ""
      }
    </div>
  </div>
  )
}
