const { serverUrl, port } = require('../util/API.json');


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