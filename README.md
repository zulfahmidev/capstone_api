# Documentation Rest API - Arahku  

## List of Contents
- Authentication
  - [Register Account](#register-account)
  - [Login Account](#login-account)
  - [Get Logged In Account Data](#get-logged-in-account-data) 
  - [Forgot Password](#forgot-password)
  - [Reset Password](#reset-password)

- User Account
  - [Get User Account](#get-user-account)
  - [Edit User Account](#edit-user-account)

- Major
  - [Get Majors](#get-majors)
  - [Get Major By Id](#get-major-by-id)

- Form
  - [Get Forms](#get-all-forms)
  - [Get Form By Slug](#get-form-by-slug)

- Response
  - [Get Responses](#get-all-responses)
  - [Send Response](#send-response)

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
### isi token
```
masukan token <barier token : "token">
```
### Reponse
```
{
    "data": {
        "address": "account_address**",
        "birth_date": "Sat, 02 Feb 2002 00:00:00 GMT",
        "created_at": "Sun, 28 May 2023 22:51:06 GMT",
        "email": "account_email**",
        "id": user_id**
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
### isi token
```
masukan token <barier token : "token">
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
        "id": user_id**
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

## Get Majors
### Endpoint
```
GET <BASE_URL>/major
```
### Headers
```
Content-Type:application/json
```
### Request <Optional>
```
{
    "search": "<search_key>",
}
```
### Response
```
{
    "data": [
        {
            "created_at": "Mon, 29 May 2023 12:14:14 GMT",
            "description": "description**",
            "id": major_id**,
            "name": "major_name**"
        }
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Get Major By Id
### Endpoint
```
GET <BASE_URL>/major/<id>
```
### Headers
```
Content-Type:application/json
```
### Response
```
{
    "data": {
        "created_at": "Mon, 29 May 2023 12:14:14 GMT",
        "description": "description**",
        "id": major_id**,
        "name": "major_name**"
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Get Forms
### Endpoint
```
GET <BASE_URL>/form/
```
### Response
```
{
    "data": [
        {
            "description": "**description",
            "id": **form_id,
            "slug": **form_slug,
            "title": "**title"
        },
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Get Form By Slug
### Endpoint
```
GET <BASE_URL>/form/<slug>
```
### Response
```
{
    "data": {
        "created_at": "Mon, 05 Jun 2023 10:00:53 GMT",
        "description": "**description",
        "id": **form_id,
        "slug": "**form_slug",
        "title": "**title",
        "fields": [
            {
                "id": **field_id,
                "label": "**label_or_question",
                "options": [
                    {
                        "id": **option_id,
                        "value": "**value"
                    },

                    ...
                ]

                ...
            },
        ]
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Get Form Responses
### Endpoint
```
GET <BASE_URL>/form/response/<form_id>
```
### Response
```
{
    "data": [
        {
            "created_at": "Mon, 05 Jun 2023 10:14:10 GMT",
            "form_id": {
                "id": **form_id,
                "title": "**form_title"
            },
            "id": 1,
            "result": "**result",
            "user_id": {
                "id": **user_id,
                "name": "**username"
            },
            "responses": [
                {
                    "created_at": "Mon, 05 Jun 2023 10:14:10 GMT",
                    "id": 1,
                    "option_id": 1,
                    "response_id": 1
                }

                ...
            ]
        }
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Send Response
### Endpoint
```
POST <BASE_URL>/form/response
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "user_id": **user_id,
    "form_id": **form_id,
    "responses": [
        {
            "field_id": **field_id,
            "option_id": **option_id
        },

        ...
    ]
}
```
### Response
```
{
    "data": {
        "created_at": "Mon, 05 Jun 2023 10:14:10 GMT",
        "form_id": {
            "id": **form_id,
            "title": "**form_title"
        },
        "id": 1,
        "result": "**result",
        "user_id": {
            "id": **user_id,
            "name": "**username"
        },
        "responses": [
            {
                "created_at": "Mon, 05 Jun 2023 10:14:10 GMT",
                "id": **response_answer_id,
                "option_id": **option_id,
                "response_id": **response_id
            }

            ...
        ]
    },
    "message": "Response successfully sended.",
    "status": true
}
```
