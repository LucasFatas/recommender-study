const { serverUrl, port } = require('../util/API.json');


export const logIn = async (credentials) => {


var jsonData = {
    "usersname": credentials.username,
    "password": credentials.password
  }

    console.log(credentials);
    try {
        const response = await fetch(`${serverUrl}:${port}/dashboard/login`, {
            method: 'POST',
            mode: 'no-cors',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData),
        })
        .then(res => res.json())
        .then(data => console.log(data));
    } catch (error) {
        console.log(error.response.status)
        console.log(error.toString());
        console.log(error instanceof Error);
        
        return error

    }
}