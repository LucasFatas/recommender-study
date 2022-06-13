 ## Sprint retrospective group 2A

### Iteration number 4


|  user story # |  task | task assigned to  | estimated effort  | actual effort  | done | note |
|---|---|---|---|---|---|---|
| 26 split questionnaire based on type  | Refactor Questionnaire and QuestionnarePage components | Diego Viero | 2h  | 3h  | Yes  |  |
| 26 split questionnaire based on type  | Implement logic for having 2 questionnaires | Diego Viero | 3h  | 5h  | Yes  |  |
| 26 split questionnaire based on type  | Implement randomness in first questionnaire | Diego Viero | 1h  | 1h  | Yes  |  |
| 25 implement logic to handle different batches | Add variable parameter to select current batch and implement logic to display correct pages based on that | Diego Viero | 1h  | 1h  | Yes  |  |
| 17 Deploy Application  | Deploy Back End on Server  | Lucas Fatas  | 2h  | 4h  | Yes | This is just a mock and the real app will be deployed later once the product is finished |
| 17 Deploy Application  |  Run server on hosting server | Diego Viero  | 1h  | 1h  | Yes  |  |
| 17 Deploy Application  |  Handle routing between pages | Diego Viero  | 3h  | 4h  |   Yes  |  |
| 27 Get Pipeline Working | try to implement a test to have a pipeline working | Kenzo Boudier | 2h | 10h | no | Ran into many problems to implement a single test on the front end will only focus on it next week |
| 9 User Matching Process  | Retrieve Playlist from Back End  | Kenzo Boudier | 4h  | 5h  | Yes  ||
| 8 Retrieve Batch 2 Data  | API endpoint to send CSV file  | Daniel Puente  | 4h  | 5h  | Yes  | Once retrieved from the database, some formatting is done in this part.  |
| 8 Retrieve Batch 2 Data  | Retrieve and format necessary data from database | Daniel Puente  | 5h  | 6h  | Yes  | Complicated SQL query created with temporary tables and joining afterwards. |
| 27 Get Pipeline Working  | Organize test into test suite that can be run with a command  |  Lucas Fatas | 2h  | 2h  | Yes  |   |
| 27 Get Pipeline Working  | Refactor test and ensure they are working properly with test_database  | Lucas Fatas  | 5h  | 1h  | No  | Refactoring is done but test are more out of dated then we thought so separate issue will be created next sprint for updating/adding test  |
| 1 Dashboard Log In  |  Save login credentials for researcher securely | Lucas Fatas  | 3h  | 5h  | yes  |  | 
| 1 Dashboard Log In  | API call to get token and check login credentials | Lucas Fatas | 4h | 4h  |  yes |   |   
| 1 Dashboard Log In  | create design | Nathaniël De Leeuw | 3h | 3h  |  yes |   |   
| 1 Dashboard Log In  | implement login interface | Nathaniël De Leeuw | 2h | 3h  |  yes |   |   
| 1 Dashboard Log In  | handle wrong logins | Nathaniël De Leeuw | 1h | 1h  |  yes | should test the back-end communication  |   
| 1 Dashboard Log In  | redirect good logins | Nathaniël De Leeuw | 1h | 3h  |  yes | should test the back-end communication  |   
| 7/8 Retrieve Batch 1/2 Data  | make general dashboard interface | Nathaniël De Leeuw  | 6h  | 6h  | Yes  | | 
| 7/8 Retrieve Batch 1/2 Data  | download button | Nathaniël De Leeuw  | 2h  | 2h  | Yes  |  |
| 28 Fix controller and service methods  | add matching storing  | Lucas Fatas and Kenzo Boudier  | 2h  | 6h  | yes  |   |
| 28 Fix controller and service methods  | update sql of changed names | Daniel Puente | 3h  | 4h  | yes  | All keywords in uppercase, rest of names in camelcase. DashboardService.py methods updated in branch related to issues #7 and #8. |
| 28 Fix controller and service methods  | Make all necessary controller methods POST methods.  | Daniel Puente  | 2h  | 3h  | yes  |  The methods in DashboardController have been updated in branch related to issue #8. |


#### Main problems encountered


##### Problem 1
- Description: Pipeline Implementation
- Reaction: Was able to resolve some of the problems in the pipeline after many hours of searching so not much was done unfortunately 
 
##### Problem 2
- Description: The Sql statements were different across the methods
- Reaction: Daniel was able to unify all the sql statements and posted them in a doc, the format will stay however the content is susceptible to be modified depending on the needs
 

##### Problem 3
- Description: Logic after splitting questionnaire - Front end
- Reaction: The questionnaire had to be divided into personality and values questionnaire. This process involved some convoluted changes that took more time than expected. Mainly ordering them randomly took time since we couldn’t know before-hand the order.

#### Adjustments for next sprint
- Work on pipeline to have it running
- Try to meet a bit more as we work better together
- As a lot of tasks are being done communicate it more in the group chat so we have a clear idea of what is done
- Start to connect both ends and work 
- Try to be more rigorous with the final draft 


