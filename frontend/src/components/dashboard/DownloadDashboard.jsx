import React from 'react';
import { retrieveCSV } from "../../controller/dashboardController";
import { CSVLink } from 'react-csv';

const buttonStyle = 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 my-2 px-4 rounded-full text-white text-center mt-4';

export const DownloadDashboard = (props) => {

  const {
    downloadData, 
    setDataToDownload, 
    setBatchToDownload, 
    batches, 
    canDownload, 
    CSVToDownload, 
    batchToDownload, 
    dataToDownload, 
    setCSVToDownload, 
    setCanDownload, 
    date
  } = props;

  return (
    <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
    <span className="text-white text-center text-xl"> Download Data </span>
    <div className='flex'>
      <span className="text-white pr-3"> Batch: </span>
      {batches.map((batch, index) => 
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
    {
      batchToDownload ? 
        <div className='flex'>
          <span className="text-white pr-3"> Data: </span>
          {downloadData.map((data, index) => {
            if ((batchToDownload === "1" && data === "Playlist Rating&Feedback") ||  
              (batchToDownload === "1" && data === "Song Ratings") )
              return <></>
            else 
              return(
              //playlist rating & feedback, song ratings
              <div key={index} className='pr-3 '>
                <input 
                  type="radio" 
                  value={data}
                  name={"data"}
                  onChange={e => setDataToDownload(e.target.value)}
                /> 
                <span className="text-white"> {data} </span>
              </div>
            )
          })}
        </div>
      : ""
    }
    <button className={buttonStyle} onClick={() => retrieveCSV(batchToDownload, dataToDownload, setCSVToDownload, setCanDownload)} >
      Retrieve Data
    </button>  
    {
      canDownload
      ?
        <div className='text-center'>
          <CSVLink
            data={CSVToDownload}
            separator={","}
            enclosingCharacter={`"`}
            filename={dataToDownload + date() + ".csv"}
          >
            <button className={buttonStyle} onClick={() => setCanDownload(false)} >
              Download
            </button> 
          </CSVLink>
        </div>
      : ""
    }
    
  </div>
  )
}
