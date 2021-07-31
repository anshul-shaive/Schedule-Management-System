Schedule Management System
------------------
### Running Instructions:

 - Run `pip install -r requirements.txt`
 - `set FLASK_APP = app`
 - Set the environment variable SCHEDULE\_DB\_URI with the url for MySQL database (mysql://user:password@host/database_name)
 - Run `flask run` in cmd


### Working:

 - ##### Schedule Meeting:

   - Send a POST request to the route <b>/schedule_meet</b> with JSON data in body (In Postman select Body -> raw -> select JSON)
<br/>
   Example: <br/>
   `{
    "RoomID":"R1",
    "Date":"31 July 2021",
    "StartTime":"2:30",
    "EndTime":"4:00",
    "Participants":"['Jim','Dwight']"
}`
 
   - Participants field is optional. Participants can also be added after meeting is scheduled.
   - Time should be in a 24 hours HH:MM format.
   - Rooms should be selected from R1 to R5 or r1 to r5.
 - #### Check Availability of Participants

   - Send a POST request to the route <b>/check_avail</b> with JSON data in body:
   </br> Example: </br>
    `{   "Name":"Michael",
    "Date":"1 August 2021",
    "StartTime":"11:30",
    "EndTime":"12:00"
}`
   - The above request will check if Michael is available for a 30 min meeting on 1st August.
   
 - #### Add another person to a scheduled meeting

   - Send a POST request to the route <b>/add_participant</b> with JSON data in body:
   </br> Example: </br>
    `{   "Name":"Oscar",
    "MeetID":"2"
}`
   - The above request sends the name of person to be included in an already scheduled meeting with id 2.
   
   


   
