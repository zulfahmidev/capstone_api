# Documentation Rest API - Arahku

## List of Contents
- [Register Account](#register-account)
- [Login Account](#login-account)
- [Show Logged In Account Data](#show-logged-in-account-data)
- [Forgot Password](#forgot-password)
- [Reset Password](#reset-password)
- [Show User Account](#show-user-account)
- [Edit User Account](#edit-user-account)

## Register Account

### Endpoint
```
POST <BASE_URL>/auth/register
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<NAME>",
    "email": "<EMAIL>",
    "password": "<PASSWORD>",
    "phone": "<NO HP>",
    "address": "<ADDRESS>",
    "birth_date": "<YYYY-MM-DD>"
}
```
### Response
```
{
    "message": "Registration successful! Please check your mailbox for email verification",
    "success": true
}
```
***Note:***
Check your mailbox after registered for verify your email. This is an example email verification:
![image](https://github.com/zulfahmidev/capstone_api/assets/109580466/8936f40f-4911-48f3-b702-40fd1465d7d2)

## Login Account
### Endpoint
```
POST <BASE_URL>/auth/login
```
### Headers
```
Content-Type:application/json
``` 
### Request
```
{
    "email": "<EMAIL>",
    "password": "<PASSWORD>"
}
```
### Response
```
{
    "data": {
        "access_token": "access_token**"
    },
    "message": "Your have succesfully logged in.",
    "success": true
}
```

## Show Logged In Account Data
### Endpoint
```
GET <BASE_URL>/auth/me
```
### Reponse
```
{
    "data": {
        "address": "account_address**",
        "birth_date": "Sat, 02 Feb 2002 00:00:00 GMT",
        "created_at": "Sun, 28 May 2023 22:51:06 GMT",
        "email": "account_email**",
        "id": "user_id**"
        "name": "account_name**",
        "phone": "phone*",
        "picture": "picture_url**"
    },
    "message": "Data loaded successfully.",
    "status": true
}
```
## Forgot Password
### Endpoint
```
POST <BASE_URL>/auth/forgot-password
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "email": "<EMAIL>"
}
```
### Response
```
{
    "data": {
        "reset_token": "reset_token**"
    },
    "message": "Token reset has been successfully generated.",
    "status": true
}
```

## Reset Password
### Endpoint
```
POST <BASE_URL>/auth/reset-password/<token>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "password": "<NEW PASSWORD>"
}
```
### Response
```
{
    "message": "Password successfully changed.",
    "status": true
}
```

## Show User Account
### Endpoint
```
GET <BASE_URL>/user/<id>
```
### Response
```
{
    "data": {
        "address": "account_address**",
        "birth_date": "Sat, 02 Feb 2002 00:00:00 GMT",
        "created_at": "Sun, 28 May 2023 22:51:06 GMT",
        "email": "account_email**",
        "id": "user_id**"
        "name": "account_name**",
        "phone": "phone*",
        "picture": "picture_url**"
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Edit User Account
### Endpoint
```
PUT <BASE_URL>/user/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<NAME>",
    "email": "<EMAIL>",
    "phone": "<NO HP>",
    "address": "<ADDRESS>",
    "birth_date": "<YYYY-MM-DD>",
    "picture": "<BASE64_IMAGE>",
}
```
### Response
```
{
    "message": "Data succesfully updated.",
    "status": true
}
```