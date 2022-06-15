## Sprint retrospective group 2A

### Iteration number 1


|  user story # |  task | task assigned to  | estimated effort  | actual effort  | done | note |
|---|---|---|---|---|---|---|
| 5 Navigate pages | Design questionnaire page  | Nathaniël de Leeuw, Diego Viero  | 6h  | 8h  |  yes |   |
| 5 Navigate pages | Handle user going to next page | Nathaniël de Leeuw, Diego Viero  | 2h  | 2h  |  yes |   |
| 5 Navigate pages |  Handle user going to previous page| Nathaniël de Leeuw, Diego Viero  | 3h  | 4h  |  yes |   |
| 6 Edit answers | Design   | Nathaniël de Leeuw, Diego Viero  | 2h  | 2h  | yes  |   |
| 6 Edit answers | hasn't answered a question and tries to change it  | Nathaniël de Leeuw, Diego Viero  | 1h  | 1.5h  | yes  |   |
| 6 Edit answers |  check backend has the latest change   | Nathaniël de Leeuw, Diego Viero  | 1h  | 1h  | yes  |   |
| 4 Answer questions | API Endpoint to handle submission of answers | Daniel Puente | 3h | 4,5h  | yes |  |
| 4 Answer question  | calculate and return value and personality scores  | Daniel Puente | 2.30h  | 3.45h | no | values still not computable, waiting for final list from client  |
| 4 Answer question  | Store personality and values scores | Daniel Puente, Kenzo Boudier, Lucas Fatas | 4h  | 5h  | yes | Created new tables in database and Python code to store them |
| 4 Answer question  | Create Database tables and methods to access them |Kenzo Boudier | 5h  | 6h  | yes | Created the tables in the database and the SQL statement to create/access them  |
| 4 Answer question  | Database Error handling | Daniel Puente | 4h  | 5h  | yes | Created new test tables, and exceptions for it  |
| 4 Answer question  | Create user | Lucas Fatas, Daniel Puente | 4h  | 5h  | yes | Created tables in database and Python code to store users |
| 4 Answer question | Setting up Back-End | Lucas | 3h  | 3h  | yes | This is just the skeleton and is susceptible to modification |
| 4 Answer question | Test | Lucas Fatas, Daniel Puente, Kenzo Boudier | 3h  | 4h  | no | Tests added for controller and service finished, not for personality calculations |
| 4 Answer question | Comments | Lucas Fatas, Daniel Puente, Kenzo Boudier | 1h  | 1h  | yes |  |
|   |   |   |   |   |   |   |

#### Main problems encountered

##### Problem 1
- Description: We don't have the questionnaires so we were not able to complete the calculations of the personality and value vector
- Reaction: We told Sandy that a questionnaire needs to be decided as soon as possible and she told she would get back to us in a few days with a final decision

##### Problem 2
- Description: Didn't complete some tasks but this was the first sprint and a lot of us are working with new technologies
- Reaction: Now that we are more familiar with the technologies this should not be an issue for next sprint

##### Problem 3
- Description: Most of our work was done together in groups. Task were not divided individually as much as they could be. 
- Reaction: We were less efficient then we could have been


##### Problem 4
- Description: The database tables are a draft and therefore are very susceptible to changing in the future 
- Reaction: We should try to unify the sql statements and create a file to store all the tables in a document 


#### Adjustments for next sprint 
- The chair of the meeting next week will be more directive during the meeting
- Nothing to say about the minute - taker
- We will ask Sandy for the final questionnaires so that we can implement them.
- Ask Sandy on the matching metrics and the ones we should implement
- We will divide the tasks more clearly so as not to have so much overlap between us.
- Be more vigorous when coding and add more comments to code

