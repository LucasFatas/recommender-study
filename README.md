# Recommender

## Name
RecMix a Value Based Recommender for Music

## Description
The objective of this project is to create a web application. The website would consist of two parts a questionnaire and a rating part. The questionnaire would allow to determine the values and personality of an individual. The rating part would consist of rating and answering some questions about 3 playlist that are 5 songs long. One playlist comes from a user that has values analogue to the participant, another playlist comes from a user with a similar personality and the last playlist is chosen at random. This website is an experiment for PhD student Sandy Manolios to see if people appreciate music of others with similar values. To determin the values of an individual the HEXACO was chosen, more information can be found here: http://hexaco.org./ . The PVQ allows to determin the personality of users any additional information can be found here: LINK . On the internet there are a multitude of different websites to see your values and personality however this website is the only one that uses values and personality to recommend playlist. This allows participants to not only see their values and personality but additionally discover music they might appreciate. To get the music snippets and favorite songs pf each participant we use the Sportify api, the following link will show the doucumentation of the api: https://developer.spotify.com/documentation/web-api/reference/. 

## Installation Frontend

## Installation Backend
To get the backend running smoothly, make sure to install and use python 3.8

To install the python packages install pip and run the command:

pip install requirements.txt

The requirements.txt file is in the backend directory and contains all the packages used in the backend.

## Run Frontend 

## Run Backend
The backend can be run with the command:

python main.py

main.py is in the backend directory

## Deploy application
The application is deployed on a Bastian server provided by TU Delft. To get access to the credentials to the recmix application to be able to connect with SHH and SFTP contact:

Bart Vastenhouw
B.Vastenhouw@tudelft.nl

## Usage
The use of this project is to be used by anyone with a spotify account. The website has two purposes. The first purpose is for the PhD student Sandy Manolios, this website is an expirement to aid her in her thesis so she is able to monitor the entire website. From the dashboard, she is able to change the matching metric, the batch and export data collected on the website. The second purpose is for the participants of the experiance. Participants will first be directed to a consent page explaining them what they are about to do and the experiment thay areparticipating in. Then an introduction page of either the personality of value test will appear and direct them to a questionnaire. After completting both questionnaire, participants will be able to see thier results as a gaph. Next they will be shown three playlists that the user has to complete in order to finish the experiment.    

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
This project is open to contribution however any contribution must still be in the aim of helping PhD student Sandy Manolios with her expirement.
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
This project was made possible because of Lucas Fatas, Diego Vieron, Daniel Puente Barajas, Nathaniel De Leeuw and Kenzo Boudier. Additionly this project was suppervised by a great TA Bianca Cosma and TU Coach Gosia Migut to make sure that the group was going in the right direction. 

## Project status
The application is at a stage where it would be ready for use, but we recommend that more user testing is completed and that a developer will be needed to ensure the application runs properly during the study. 
