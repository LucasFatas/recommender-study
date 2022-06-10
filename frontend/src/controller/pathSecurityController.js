const { dev } = require('../util/dev.json');

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
        else if(url.includes("introduction") && url === "introduction/" + type){
          console.log("you are in" + url)
    
        }
        else{
          console.log("you are redirected to", url)
          navigate(sessionStorage.getItem("currentUrl"))
    
        }
    }
   

}

const helperFunction = (navigate, url) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== url){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
        }
    else
        {
            console.log("you are in", sessionStorage.getItem("currentUrl"))
        }
    }
  
}

export const websiteIntroductionSecurity = (navigate) => {
    helperFunction(navigate, "/websiteIntroduction")
}

export const constentPageSecurity = (navigate) => {
    helperFunction(navigate, "/consentPage")
    
}

export const thanksPageSecurity = (navigate) => {
    helperFunction(navigate, "/thanks")
}

export const questionnaireSecurity = (navigate, initialPath) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== "/questionnaire"){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
        }
        else
        {
            console.log("you are in", sessionStorage.getItem("currentUrl"))
            sessionStorage.setItem("currentUrl", "/questionnaire/" + initialPath + "/page1")
        }
    }
    
}

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

export const questionnaireResultSecurity = (navigate) => {
    helperFunction(navigate, "/questionnaire/results")
  
}

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

export const recommenderSecurity = (navigate) => {
    if(!dev) {
        if(sessionStorage.getItem("currentUrl") !== "/recommender"){
            console.log("you are redirected to", sessionStorage.getItem("currentUrl"))
            navigate(sessionStorage.getItem("currentUrl"))
          }
        else
          {
            console.log("you are in", sessionStorage.getItem("currentUrl"))
            sessionStorage.setItem("currentUrl", "/recommender/page1")
          }
    }
   
  
}