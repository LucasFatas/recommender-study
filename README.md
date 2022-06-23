# Recommender

## Name
RecMix a Value Based Recommender for Music

## Description
The objective of this project is to create a web application. The website consists of three parts: a questionnaire, a recommender and rating system, and a dashboard. The questionnaire allows to determine the values and personality of an individual. The rating part consists of rating and answering some questions about 3 playlist that are 5 songs long. One playlist comes from a user that has values analogue to the participant; another playlist comes from a user with a similar personality; and the last playlist is chosen at random. The dashboard part belongs to the experiment manipulation and management, and will solely be accessed by the researcher of this experiment - and our client - PhD candidate Sandy Manolios. 

Her research aims to prove if people appreciate music of people with similar Portrait Values. To determine the personality of an individual the HEXACO model was chosen,  and more information can be found here: http://hexaco.org./ . The PVQ allows to determine the Portrait Values of users, and additional information can be found here: http://wiki.mgto.org/doku.php/portrait_value_questionnaire_pvq?msclkid=1ae65174d05e11ec82efdd1b9bb2c30c. 

When looking at inspiration from other websites, we encountered multitude of different websites to calculate your value and personality scores. However this website is the only one that uses these scores to recommend music and assess the quality of the recommendations. This allows participants not only to see their values and personality, but also discover music they might appreciate.

To get the music snippets and favorite songs pf each participant we use the Spotify API. The following link will show the documentation of the api: https://developer.spotify.com/documentation/web-api/reference/.

## Installation Frontend
To install front-end application, go to the /frontend folder and use yarn or npm to run the command:
  
````
yarn install
````
 
 or 
 
````
npm install
````

respectively. <br />
This will install the packages on your computer. 



## Installation Backend
To get the backend running smoothly, make sure to install and use python 3.8. <br />
To install the python packages install pip and run the command:

````
pip install requirements.txt
````

The requirements.txt file is in the backend directory and contains all the packages used in the backend.

## Run Frontend 
To run the front-end application, go to the /frontend folder on the console and run the command:

````
yarn start-lin
````

or 
    
````
yarn start-win
````

depending on if you are using linux or windows. <br />
This will start the application on port 5000. Go then to your favorite browser and open the application with the right url and port 5000. <br />
To build the front-end application, go to the /frontend folder and run 

````
yarn build
````

It will create the build folder and save the builded application in it. When you want to deploy the application, you only need to take the files of the build folder. 

## Run Backend
The backend can be run with the command:

````
python main.py
````

main.py is in the backend directory

## Deploy application
The application is deployed on a Bastian server provided by TU Delft. To get access to the credentials to the recmix application you need to connect with SHH and SFTP. In order to do that you can contact:

Bart Vastenhouw <br />
B.Vastenhouw@tudelft.nl

## Usage
This project divides is divided into two different and clearly distinguishable usage cases. The first one is the experiment management use. It is intended for PhD student Sandy Manolios  to aid her in her thesis so that she is able to monitor the entire website, and the parameters involved in the experiment walkthrough. From the dashboard, she is able to change the matching metric, the batch and export data collected on the website.

The second use case is for the participants of the experiment. Participants will first be directed to a consent page explaining them what they are about to do and information about the experiment thay are participating in. Then an introduction page of either the personality of value test will appear and direct them to a questionnaire. After completing both questionnaire, participants will be able to see their results as a graph. Next, and only if the participant is fulfilling the experiment in its second batch, they will be shown three playlists that they have to rate in order to finish the experiment.

This second usage case is how the app will be handled by most of the users. The dashboard will only be used by the client, and the rest of the users of our app will go through the experiment after receiving the link from a Prolific post made by Ms Manolios. <br /><br />

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
This project is open to contribution however any contribution must still be in the aim of helping PhD student Sandy Manolios with her expirement.
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
This project was made possible because of Lucas Fatas, Diego Vieron, Daniel Puente Barajas, Nathaniël De Leeuw and Kenzo Boudier. Additionaly this project was supervised by TA Bianca Cosma and TU Coach Gosia Migut to make sure that the group was going in the right direction. 

## Project status
The application is at a ready stage, and is fully deployed, but we recommend that more user testing is completed and that a helping developer is employed to ensure the application in a smoother way during the study. 
