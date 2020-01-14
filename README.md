# SAARTHI API
## User Profile API

### End point URL 
http://rashmi1604.pythonanywhere.com/api/users_create

### Header
* Content-Type : application/json
* secret : rashmii

### Sample Response 
* HTTPS Status : 201 Created
* {
    "user_id": "viveke341",
    "first_name": "vivek",
    "last_name": "kumar",
    "email_id": "vivek123@gmail.com"
}

## Chat History API

### End point URL 
http://rashmi1604.pythonanywhere.com//api/chat_history

### Header
* Content-Type : application/json
* secret : rashmii

### Sample Response 
* HTTPS Status : 201 Created
* {
    "user_id": 1,
    "msg": "train no. 12296 on 13-01-2020 from bxr",
    "reply": "You queried for Train: Departed from Bhadanpur at 08:59 14-Jan. 451 Kms. ahead of Buxar."
}
