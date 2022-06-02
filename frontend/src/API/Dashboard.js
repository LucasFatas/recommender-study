const { serverUrl, port } = require('../util/API.json');


export const getSongs = async (batchId, token) => {
    console.log(batchId);
    try {
        const response = await fetch(`${serverUrl}:${port}/dashboard/songs?batchId=${batchId}`, {
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

export const getSongRatings = async () => {
    console.log("ratings")
    try {
        const response = await fetch(`${serverUrl}:${port}/dashboard/songRatings`, {
            method: 'GET',
            headers: {
                'Content-Type': 'text/csv'
            },
        });
        console.log(response);
        return response
    } catch (error) {
        return console.log(error);
    }
}

export const getScores = async (batchId) => {
    console.log(batchId);
    try {
        const response = await fetch(`${serverUrl}/dashboard/scores`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(batchId),
        });
        console.log(response);
        return response
    } catch (error) {
        console.log(error);
    }
}

export const getAnswers = async (batchId) => {
    console.log(batchId);
    try {
        const response = await fetch(`${serverUrl}/dashboard/answers`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(batchId),
        });
        console.log(response);
        return response
    } catch (error) {
        console.log(error);
    }
}

export const getMatchData = async () => {
    try {
        const response = await fetch(`${serverUrl}:${port}/dashboard/match`, {
            method: 'GET',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
        });
        console.log(response);
        return response
    } catch (error) {
        return console.log(error);
    }
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