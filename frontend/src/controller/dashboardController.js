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


export const isLoggedIn = (token, navigate) => {
    
      if(!token)
        navigate("/login")
      else
        console.log('authentication is a success');
}


export const retrieveCSV = async (batchToDownload, dataToDownload, setCSVToDownload, setCanDownload) => {
  console.log("download CSV")
  console.log(batchToDownload, dataToDownload)

  switch(dataToDownload) {
    case "Songs":
      await getSongs(batchToDownload, sessionStorage.getItem("token")).then(res =>{

        setCSVToDownload(res.toString())
        setCanDownload(true)
      })
      
     
      break;
    case "Q&A":
      await getAnswers(batchToDownload, sessionStorage.getItem("token")).then(res =>{

        setCSVToDownload(res.toString())
        setCanDownload(true)
      })
      break;
    case "Playlist Rating&Feedback":
      if(batchToDownload === "1"){
        console.log("this batch has not this type of data : " + dataToDownload)
      }else{
        await getMatchData(sessionStorage.getItem("token")).then(res =>{

          setCSVToDownload(res.toString())
          setCanDownload(true)
        })
      }
      break;
    case "Scores":
      await getScores(batchToDownload, sessionStorage.getItem("token")).then(res =>{

        setCSVToDownload(res.toString())
        setCanDownload(true)
      })
      break;
    case "Song Ratings":
      if(batchToDownload === "1"){
        console.log("this batch has not this type of data : " + dataToDownload)
      }else{
        await getSongRatings(sessionStorage.getItem("token")).then(res =>{

          setCSVToDownload(res.toString())
          setCanDownload(true)
        })
      }
      break;
    default:
      // code block
      console.log("error word does not exist: " ,dataToDownload)
  }
}