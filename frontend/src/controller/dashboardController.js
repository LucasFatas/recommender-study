

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


export const isLogedIn = (token, navigate) => {
    
      if(!token)
        navigate("/login")
      else
        console.log('authentication is a success');
}