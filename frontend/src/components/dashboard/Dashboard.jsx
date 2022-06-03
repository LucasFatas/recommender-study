import React from 'react';
import { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';
import { isLoggedIn, retrieveCSV } from "../../controller/dashboardController";
import { CSVLink} from 'react-csv'

export const Dashboard = () => {
  

  const navigate = useNavigate()
 
  
  useEffect(() => {
    isLoggedIn(sessionStorage.getItem("token"), navigate)

  }, [])

  const logout = () => {
    sessionStorage.removeItem("token")
    navigate("/login")
  };
  const date = () => {
    var currentdate = new Date(); 
    return currentdate.getDate() + "/"
                  + (currentdate.getMonth()+1)  + "/" 
                  + currentdate.getFullYear() + " @ "  
                  + currentdate.getHours() + ":"  
                  + currentdate.getMinutes() + ":" 
                  + currentdate.getSeconds();
  }
  

// This part is temporary, it is going to change next sprint
  const batchNumber = 1
  const batchUsers = 1
  const batchMetric = "euclidian"
  const batchType = "Questionnaire"

  const downloadData = ["Songs", "Q&A", "Playlist Rating&Feedback", "Scores", "Song Ratings"]
  const batchs = [1,2]
  const metric = ["Euclidean", "Manhattan"]

  const [dataToDownload, setDataToDownload] = useState("");
  const [batchToDownload, setBatchToDownload] = useState("");
  const [metricNextBatch, setMetricNextBatch] = useState("");
  const [CSVToDownload, setCSVToDownload] = useState([]);
  const [canDownload, setCanDownload] = useState(false);
  
  const [changeBatch, setChangeBatch] = useState(false);

  const createNewBatch = () => {
    console.log("create new batch with ", metricNextBatch, "metric")
    setChangeBatch(false)
  }
  const showChangeBatchButtons = () => {
    setChangeBatch(true)
  }


  
  return (
    
  
    <div className='flex flex-col items-center justify-between py-28'>
      <div className='flex rounded-[20px] mx-10 px-5 py-6 border-solid border-4 border-gray-300 bg-gray-700' >
        <div className='flex flex-col'>
          <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
          
         
            {/* This is temporary, It is going to change Next Sprint in branch 33 Experiment Parameters  */}
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
          {!changeBatch?
          <div className='py-2 text-center'>
            <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={showChangeBatchButtons} >
              <div className='grid place-items-center '>
                <span className="text-white"> New Batch </span>
              </div>
            </button> 
            
            
          </div>
        :
        <>
          <div className='flex py-2'>
            <span className="text-white pr-3"> Metric: </span>
            {metric.map((metric, index) => 
              (<div className='pr-3 '>
                <input 
                  type="radio" 
                  // className={inputStyle} 
                  value={metric}
                  name={"metric"}
                  onChange={e => setMetricNextBatch(e.target.value)}
                /> 
                <span className="text-white"> {metric} </span>
              </div>)
            )}
          </div>
          <div className='py-2 text-center'>
          <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={createNewBatch} >
            <div className='grid place-items-center '>
              <span className="text-white"> Create and Change to New Batch </span>
            </div>
          </button> 
          
        </div>
       </>


          }
          
          
        </div>
        
        <div className='flex flex-col rounded-[10px] mx-10 px-12 py-6 border-solid border-2 border-gray-300 bg-gray-700' >
          <span className="text-white text-center text-xl"> Download Data </span>
          <div className='flex'>
            <span className="text-white pr-3"> Data: </span>
            {downloadData.map((data, index) => 
              (<div key={index} className='pr-3 '>
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
          {!canDownload?
          <></>
          :
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
          }
          
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