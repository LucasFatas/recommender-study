const { serverUrl, port } = require('../util/API.json');


const retrieveCSVHelperFunction = async ({batchId, token, endpoint}) => {

    const uri = typeof batchId === 'undefined' || batchId === null
        ? `${serverUrl}:${port}/dashboard/${endpoint}`
        : `${serverUrl}:${port}/dashboard/${endpoint}?batchId=${batchId}`;
        
    try {
        const response = await fetch(uri, {
            method: 'GET',
            headers: {
                'Authorization': "Bearer " + token,
                'Content-Type': 'text/csv'
                
            }
        }).then(res => res.text());

        console.log(response);

        return response        
    } catch (error) {
        console.log(error);
    }
}

export const getSongs = async (batchId, token) => retrieveCSVHelperFunction({batchId : batchId, token : token, endpoint : "songs"})

export const getSongRatings = async (token) => retrieveCSVHelperFunction({token : token, endpoint : "songRatings"})

export const getScores = async (batchId, token) => retrieveCSVHelperFunction({token : token, batchId : batchId, endpoint : "scores"})

export const getAnswers = async (batchId, token) => retrieveCSVHelperFunction({token : token, batchId : batchId, endpoint : "answers"})

export const getMatchData = async (token) => retrieveCSVHelperFunction({token : token, endpoint : "match"})

const getHelper = async ({setter, parameter, token, batchId, endpoint}) => {

    const uri = typeof batchId === 'undefined' || batchId === null
        ? `${serverUrl}:${port}/dashboard/${endpoint}`
        : `${serverUrl}:${port}/dashboard/${endpoint}?batchId=${batchId}`;

    const header = typeof token === 'undefined' || token === null
        ? 
            {'Content-Type': 'application/json'}
        :
            {
                'Authorization': "Bearer " + token,
                'Content-Type': 'application/json',
            };
        
    try {
        await fetch(uri, {
            method: 'GET',
            headers: header
        })
        .then(res => res.json())
        .then(data => setter(data[parameter]));

    } catch (error) {
        console.log(error);
    }
}

export const getBatch = async (setBatch, parameter) => getHelper({setter : setBatch, parameter : parameter , endpoint : "batch"})

export const getUsers = async (setBatch, parameter, token, batchId) => getHelper({setter : setBatch, parameter : parameter, token : token, batchId : batchId , endpoint : "users"})

export const getMetric = async (setBatch, parameter, token) => getHelper({setter : setBatch, parameter : parameter, token : token, endpoint : "metric"})

export const setBatch = async (setBatch, setMetric, setChangeBatch, setMetricNextBatch, token, metric) => {

    const uri = `${serverUrl}:${port}/dashboard/setBatch?metric=${metric}`
        
    try {
        await fetch(uri, {
            method: 'GET',
            headers: {
                'Authorization': "Bearer " + token,
                'Content-Type': 'application/json'

            },
        })
        .then(res => res.json())
        .then(data => {
            setBatch(data.batch)
            setMetric(data.metric)
            setChangeBatch(false)
            setMetricNextBatch("")
        });

    } catch (error) {
        console.log(error);
    }
}

const helperPost = async (uri, token) => {
    try {
        await fetch(`${serverUrl}:${port}/dashboard${uri}`, {
            method: 'POST',
            headers: {
                'Authorization': "Bearer " + token,
                'Content-Type': 'application/json'
            }
        }).then(res => res)

    } catch (error) {
        console.log(error);    
    }
}

export const revertBatch = (token, setBatchNumber) => {
    helperPost('/revert', token);
    setBatchNumber(1)
};

export const resetData = (token) => helperPost('/reset', token);

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