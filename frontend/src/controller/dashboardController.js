import { getAnswers, getMatchData, getScores, getSongRatings, getSongs } from "../API/Dashboard";


/**
 * If batch is set to 'questionnaire', set it to 'recommender and vice versa
 * @param {string} currentBatch either 'questionnaire' or 'recommender'
 * @param {*} setCurrentBatch function to change current batch
 */
export const switchBatch = (currentBatch, setCurrentBatch) => {
    currentBatch === 'questionnaire' 
        ? setCurrentBatch('recommender') 
        : setCurrentBatch('questionnaire');
}

/**
 * Check if the user is logged in, if not, she/he is redirected to the log in
 * @param {String} token is the token available in session storage, previously received by logging in
 * @param {*} navigate react function to navigate to another page
 */
export const isLoggedIn = (token, navigate) => {
    
      if(!token)
        navigate("/login")
      else
        console.log('authentication is a success');
}

/**
 * Based on the user choice, the right CSV is retrieved from teh back-end
 * @param {Int} batchToDownload the batch to download from either 1 or 2 
 * @param {String} dataToDownload the data to download
 * @param {*} setCSVToDownload Setter to change the useState
 * @param {*} setCanDownload Setter to change the useState
 */
export const retrieveCSV = async (batchToDownload, dataToDownload, setCSVToDownload, setCanDownload) => {
  console.log("download CSV")
  console.log(batchToDownload, dataToDownload)

  switch(dataToDownload) {
    case "Songs":
      await getSongs(batchToDownload, sessionStorage.getItem("token")).then(res =>{
        helperCSVDownload(res, setCSVToDownload, setCanDownload)
      })
      break;
    case "Q&A":
      await getAnswers(batchToDownload, sessionStorage.getItem("token")).then(res =>{
        helperCSVDownload(res, setCSVToDownload, setCanDownload)
      })
      break;
    case "Playlist Rating&Feedback":
      if(batchToDownload === "1"){
        console.log("this batch has not this type of data : " + dataToDownload)
      }else{
        await getMatchData(sessionStorage.getItem("token")).then(res =>{
          helperCSVDownload(res, setCSVToDownload, setCanDownload)
        })
      }
      break;
    case "Scores":
      await getScores(batchToDownload, sessionStorage.getItem("token")).then(res =>{
        helperCSVDownload(res, setCSVToDownload, setCanDownload)
      })
      break;
    case "Song Ratings":
      if(batchToDownload === "1"){
        console.log("this batch has not this type of data : " + dataToDownload)
      }else{
        await getSongRatings(sessionStorage.getItem("token")).then(res =>{
          helperCSVDownload(res, setCSVToDownload, setCanDownload)
        })
      }
      break;
    default:
      // code block
      console.log("error word does not exist: " ,dataToDownload)
  }
}

/**
 * This method calls the endpoint to change from batch 1 to batch 2 and as parameter we give the metric of batch 2 
 * there exist a revert method on the back-end, but we do not use it on the front-end
 * @param {*} setBatch Setter for Batch
 * @param {*} setBatchNumber Setter for BatchNumber
 * @param {*} setBatchMetric Setter for Metric
 * @param {*} setChangeBatch Setter for changing batchs
 * @param {*} setMetricNextBatch Setter for MetricNextBatch
 * @param {String} metricNextBatch 
 */
export const backEndCreateNewBatch = (setBatch, setBatchNumber, setBatchMetric, setChangeBatch, setMetricNextBatch, metricNextBatch) => {
  console.log("create new batch with ", metricNextBatch, "metric")
  if (metricNextBatch)
    setBatch(setBatchNumber, setBatchMetric, setChangeBatch, setMetricNextBatch,  sessionStorage.getItem("token"), metricNextBatch)
}


const helperCSVDownload = (res, setCSVToDownload, setCanDownload) => {
  setCSVToDownload(res.toString())
  setCanDownload(true)
}