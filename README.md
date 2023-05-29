# Documentation Rest API - Arahku

## List of Contents
- [Register Account](#register-account)
- [Login Account](#login-account)
- [Show Logged In Account Data](#show-logged-in-account-data)
- [Forgot Password](#forgot-password)
- [Reset Password](#reset-password)

## Register Account

### Endpoint
```
POST <URL>/auth/register
```
### Headers
```
Content-Type:application/json
```
### Example Request
```
{
    "name": "<NAME>",
    "email": "<EMAIL>",
    "password": "<PASSWORD>",
    "phone": "<NO HP>",
    "address": "<ADDRESS>",
    "birth_date": "<y-m-d>"
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
POST <URL>/auth/login
```
### Headers
```
Content-Type:application/json
``` 
### Example Request
```
{
    "email":"<EMAIL>",
    "password":"<PASSWORD>"
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
GET <URL>/auth/me
```
### Example Reponse
```
{
    "data": {
        "address": "account_address**",
        "birth_date": "Sat, 02 Feb 2002 00:00:00 GMT",
        "created_at": "Sun, 28 May 2023 22:51:06 GMT",
        "email": "account_email**",
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
POST <URL>/auth/forgot-password
```
### Headers
```
Content-Type:application/json
```
### Example Requst
```
{
    "email": "<EMAIL>"
}
```
### Response
```
{
    "body": {
        "reset_token": "900a3963e2b5a06f11988f5db15dcbe0"
    },
    "message": "Token reset has been successfully generated.",
    "status": true
}
```

## Reset Password
### Endpoint
```
POST <URL>/auth/reset-password/<token>
```
### Headers
```
Content-Type:application/json
```
### Example Request
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