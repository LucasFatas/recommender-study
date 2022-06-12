const { dev } = require('../util/dev.json');

/**
 * This method is called when the user is on one of the Introduction pages
 * It prevents the user to be on these pages in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 * @param {String} type What introdction is it for : Values, personality or Playlist
 */
export const introductionPagesSecurity = (navigate, type) => {
    if(!dev) {
        const url = sessionStorage.getItem("currentUrl")
        if(sessionStorage.getItem("userID") === null){
          console.log("you have no Id, you are redirected to the consent page")
          sessionStorage.setItem("currentUrl", "/consentPage")
          navigate("/consentPage")
        } 
        else if(url === "/introduction") {
          console.log("This is the first questionnaire")
          sessionStorage.setItem("currentUrl", "/introduction/" + type)
        }
        else if(! url === "introduction/" + type){
            console.log("you are redirected to", url)
            navigate(sessionStorage.getItem("currentUrl"))
    
        }
    }
   

}

/**
 * helper function for all the other methods of this file
 *  It prevents the user to be on this page (represented by the url) in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 * @param {String} url the current path
 */
const helperFunction = (navigate, url) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== url){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
        }
    }
  
}

/**
 *  It prevents the user to be on this page in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 */
export const websiteIntroductionSecurity = (navigate) => {
    helperFunction(navigate, "/websiteIntroduction")
}

/**
 *  It prevents the user to be on this page in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 */
export const constentPageSecurity = (navigate) => {
    helperFunction(navigate, "/consentPage")
    
}

/**
 *  It prevents the user to be on this page in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 */
export const thanksPageSecurity = (navigate) => {
    helperFunction(navigate, "/thanks")
}

/**
 *  It prevents the user to be on this page in an unauthorized way
 *  from questionnaire, it is redirected to the first questionnaire, represented by the initial path
 * @param {*} navigate React component to navigate between paths 
 * @param {String} initialPath the first questionnaire the user need to answer
 */
export const questionnaireSecurity = (navigate, initialPath) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== "/questionnaire"){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
        }
        else
        {
            sessionStorage.setItem("currentUrl", "/questionnaire/" + initialPath + "/page1")
        }
    }
    
}

/**
 * It prevents the user to be on the questionnaire pages in an unauthorized way
 * or to switch questionnaires on their own will
 * @param {*} navigate React component to navigate between paths
 * @param {String} type What introdction is it for : Values, personality or Playlist
 * @param {String} pageNumber the Page number
 */
export const questionnairePageSecurity = (navigate, type, pageNumber) => {
    if(!dev) {
        const token = sessionStorage.getItem("currentUrl")
        if(token.includes("/questionnaire/" + (type === 'values' ? 'v' : 'p'))){
            const endOfToken = parseInt(token.replace("/questionnaire/" + (type === 'values' ? 'v' : 'p') + "/page", "").replaceAll(" ", ""));
            console.log(endOfToken + typeof endOfToken)
            if(!Number.isNaN(endOfToken) && endOfToken < pageNumber){
                console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
                navigate(sessionStorage.getItem("currentUrl"))
            }
        }
        else 
        {
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
        }
    }
   
}

/**
 *  It prevents the user to be on this page in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 */
export const questionnaireResultSecurity = (navigate) => {
    helperFunction(navigate, "/questionnaire/results")
  
}

/**
 * It prevents the user to be on this page in an unauthorized way
 * @param {*} navigate  React component to navigate between paths
 * @param {*} nextPage next page it needs to navigate to
 */
export const PlaylistPageSecurity = (navigate, nextPage) => {
    if(!dev) {
        const url = sessionStorage.getItem("currentUrl")
        if(url.includes("/recommender")){
          const endOfToken = parseInt(url.replace("/recommender/page", "").replaceAll(" ", ""));
          console.log(endOfToken + typeof endOfToken)
          if(!Number.isNaN(endOfToken) && endOfToken < (nextPage - 1)){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
          }
        }else {
         
          console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
          navigate(sessionStorage.getItem("currentUrl"))
        }
    }
   
}

/**
 *  It prevents the user to be on the recommender in an unauthorized way
 * @param {*} navigate React component to navigate between paths 
 */
export const recommenderSecurity = (navigate) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== "/recommender"){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
          }
        else
          {
            sessionStorage.setItem("currentUrl", "/recommender/page1")
          }
    }
   
  
}