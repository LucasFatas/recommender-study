import React from 'react';
import { useEffect, useState } from "react";
import { useNavigate } from 'react-router-dom';
import { backEndCreateNewBatch, isLoggedIn } from "../../controller/dashboardController";
import { DownloadDashboard } from './DownloadDashboard';
import { getBatch, getMetric, getUsers, setBatch } from '../../API/Dashboard';

export const Dashboard = ({switchCurrentBatch}) => {
  

  const navigate = useNavigate()

  
  const [batchNumber, setBatchNumber] = useState("");
  const [batchUsers, setBatchUsers] = useState("");
  const [batchMetric, setBatchMetric] = useState("");

  const downloadData = ["Songs", "Q&A", "Playlist Rating&Feedback", "Scores", "Song Ratings"]
  const batchs = [1,2]
  const metric = ["Euclidean", "Manhattan"]

  const [dataToDownload, setDataToDownload] = useState("");
  const [batchToDownload, setBatchToDownload] = useState("");
  const [metricNextBatch, setMetricNextBatch] = useState("");
  const [CSVToDownload, setCSVToDownload] = useState([]);
  const [canDownload, setCanDownload] = useState(false);
  
  const [changeBatch, setChangeBatch] = useState(false);
 
  
  useEffect(() => {
    isLoggedIn(sessionStorage.getItem("token"), navigate)

    const token = sessionStorage.getItem("token")
  
    getBatch(setBatchNumber, "batch", token)
    if(batchNumber){
      getUsers(setBatchUsers, "users", token, batchNumber)
      getMetric(setBatchMetric, "metric", token)
    }

  }, [batchNumber])

  const logout = () => {
    sessionStorage.removeItem("token")
    navigate("/login")
  };
  const date = () => {
    var currentdate = new Date(); 
    return `${currentdate.getDate()}/${(currentdate.getMonth()+1)}/${currentdate.getFullYear()} `;
  }
  


  const createNewBatch = () => backEndCreateNewBatch(setBatch, setBatchNumber, setBatchMetric, setChangeBatch, setMetricNextBatch, metricNextBatch);

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
              <span className="text-white pr-3"> {batchNumber ? batchNumber : ""} </span>
            </div>
            <div className='flex'>
              <span className="text-white pr-3"> Number of users: </span>
              <span className="text-white pr-3"> {batchUsers} </span>
            </div>
            <div className='flex'>
              <span className="text-white pr-3"> Type of batch: </span>
              <span className="text-white pr-3"> {batchNumber ? (batchNumber == 1 ? "Questionnaire" : "Reccomender") : ""} </span>
            </div>
            
            
            
            <div className='flex'>
              <span className="text-white pr-3"> Metric: </span>
              <span className="text-white pr-3"> {batchMetric} </span>
            </div>
          </div>
          {
            changeBatch
            ?
              <>
                <div className='flex py-2'>
                  <span className="text-white pr-3"> Metric: </span>
                  {metric.map((metric, index) => 
                    (<div className='pr-3 '>
                      <input 
                        type="radio" 
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
            :
            (
              batchNumber == 2
              ?
                <></>
              :
            
                <div className='py-2 text-center'>
                  <button className=' bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full ' onClick={showChangeBatchButtons} >
                    <div className='grid place-items-center '>
                      <span className="text-white"> New Batch </span>
                    </div>
                  </button> 
                </div>
            )
          }          
        </div>
        <DownloadDashboard 
          downloadData={downloadData} 
          setDataToDownload={setDataToDownload} 
          setBatchToDownload={setBatchToDownload} 
          batchs={batchs} 
          canDownload={canDownload} 
          CSVToDownload={CSVToDownload} 
          batchToDownload={batchToDownload} 
          dataToDownload={dataToDownload} 
          setCSVToDownload={setCSVToDownload} 
          setCanDownload={setCanDownload} 
          date={date}
        />
        
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