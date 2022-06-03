const { serverUrl, port } = require('../util/API.json');


const retrieveCSVHelperFunction = async ({batchId, token, endpoint}) => {
    console.log(batchId);
    try {
        if (typeof batchId === 'undefined' || batchId === null){
            const response = await fetch(`${serverUrl}:${port}/dashboard/${endpoint}`, {
                method: 'GET',
                headers: {
                    'Authorization': "Bearer " + token,
                    'Content-Type': 'text/csv'
                    
                }
            }).then(res => res.text());
            console.log(response);
            return response
        }else{
            
            const response = await fetch(`${serverUrl}:${port}/dashboard/${endpoint}?batchId=${batchId}`, {
            method: 'GET',
            headers: {
                'Authorization': "Bearer " + token,
                'Content-Type': 'text/csv'
                
            }
            }).then(res => res.text());
            console.log(response);
            return response
            
        }
        
    } catch (error) {
        console.log(error);
    }
}

export const getSongs = async (batchId, token) => {
    return retrieveCSVHelperFunction({batchId : batchId, token : token, endpoint : "songs"})
}

export const getSongRatings = async (token) => {
   return retrieveCSVHelperFunction({token : token, endpoint : "songRatings"})
}

export const getScores = async (batchId, token) => {
   return retrieveCSVHelperFunction({token : token, batchId : batchId, endpoint : "scores"})
}

export const getAnswers = async (batchId, token) => {
    return retrieveCSVHelperFunction({token : token, batchId : batchId, endpoint : "answers"})
}

export const getMatchData = async (token) => {
    return retrieveCSVHelperFunction({token : token, endpoint : "match"})
}



export const logIn = async (credentials) => {


    const jsonData = {
        "username": credentials.username,
        "password": credentials.password
    }

    console.log(credentials);

    try {
        const response = await fetch(`${serverUrl}:${port}/dashboard/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData),
        }).then(res => {
            if (res.status === 401)
                return false
            return res.json()
        })
        
        return response.token

    } catch (error) {
        console.log(error);
        
        return error
    }
}