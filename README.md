# Documentation Rest API - Arahku  

## List of Contents
- Authentication
  - [Register Account](#register-account)
  - [Login Account](#login-account)
  - [Show Logged In Account Data](#show-logged-in-account-data)
  - [Forgot Password](#forgot-password)
  - [Reset Password](#reset-password)

- User Account 
  - [Show User Account](#show-user-account)
  - [Edit User Account](#edit-user-account)

- Major Category
  - [Show Major Category](#show-major-category)
  - [Add Major Category](#add-major-category)
  - [Edit Major Category](#edit-major-category)
  - [Delete Major Category](#delete-major-category)

- Major
  - [Show Major](#show-major)
  - [Add Major](#add-major)
  - [Edit Major](#edit-major)
  - [Delete Major](#delete-major)

- Form
  - [Show All Form](#show-all-form)
  - [Show Form](#show-form)
  - [Create Form](#create-form)
  - [Edit Form](#edit-form)
  - [Delete form](#delete-form)

- Field
  - [Show Field](#show-field)
  - [Create Field](#create-field)
  - [Edit Field](#edit-field)
  - [Delete Field](#delete-field)

- Option
  - [Show Option](#show-option)
  - [Create Option](#create-option)
  - [Edit Option](#edit-option)
  - [Delete Option](#delete-option)

- Response
  - [Show All Response](#show-all-response)
  - [Create Response](#create-response)

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

## Show Major Category
### Endpoint
```
GET <BASE_URL>/major/category
```
### Response
```
{
    "data": [
        {
            "created_at": "Mon, 29 May 2023 09:22:02 GMT",
            "id": major_category_id**,
            "name": "category_name**"
        }
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Add Major Category
### Endpoint
```
POST <BASE_URL>/major/category
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<CATEGORY NAME>"
}
```
### Response
```
{
    "data": {
        "created_at": "Mon, 29 May 2023 09:22:02 GMT",
        "id": major_category_id**,
        "name": "category_name**"
    },
    "message": "Category successfully created.",
    "status": true
}
```

## Edit Major Category
### Endpoint
```
PUT <BASE_URL>/major/category/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<CATEGORY NAME>"
}
```
### Response
```
{
    "message": "Category successfully updated.",
    "status": true
}
```

## Delete Major Category
### Endpoint
```
DELETE <BASE_URL>/major/category/<id>
```
### Response
```
{
    "data": [
        {
            "created_at": "Mon, 29 May 2023 09:22:02 GMT",
            "id": major_category_id**,
            "name": "category_name**"
        }
    ],
    "message": "Category successfully destroyed.",
    "status": true
}
```

## Show Major
### Endpoint
```
GET <BASE_URL>/major
```
### Response
```
{
    "data": [
        {
            "category": {
                "created_at": "Mon, 29 May 2023 09:22:02 GMT",
                "id": major_category_id**,
                "name": "category_name**"
            },
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

## Add Major
### Endpoint
```
POST <BASE_URL>/major
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<NAME>",
    "description": "<DESCRIPTION>",
    "id_category": "<MAJOR CATEGORY ID>"
}
```
### Response
```
{
    "data": {
        "category": {
            "created_at": "Mon, 29 May 2023 09:22:02 GMT",
            "id": major_category_id**,
            "name": "category_name**"
        },
        "created_at": "Mon, 29 May 2023 12:14:14 GMT",
        "description": "description**",
        "id": major_id**,
        "name": "major_name**"
    },
    "message": "Major successfully created.",
    "status": true
}
```

## Edit Major
### Endpoint
```
PUT <BASE_URL>/major/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "name": "<NAME>",
    "description": "<DESCRIPTION>",
    "id_category": "<MAJOR CATEGORY ID>"
}
```
### Response
```
{
    "data": {
        "category": {
            "created_at": "Mon, 29 May 2023 09:22:02 GMT",
            "id": major_category_id**,
            "name": "category_name**"
        },
        "created_at": "Mon, 29 May 2023 12:14:14 GMT",
        "description": "description**",
        "id": major_id**,
        "name": "major_name**"
    },
    "message": "Major successfully updated.",
    "status": true
}
```

## Delete Major
### Endpoint
```
DELETE <BASE_URL>/major/category/<id>
```
### Response
```
{
    "data": {
        "category": {
            "created_at": "Mon, 29 May 2023 09:22:02 GMT",
            "id": major_category_id**,
            "name": "category_name**"
        },
        "created_at": "Mon, 29 May 2023 12:14:14 GMT",
        "description": "description**",
        "id": major_id**,
        "name": "major_name**"
    },
    "message": "Major successfully destroyed.",
    "status": true
}
```

## Show All Form
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
            "title": "**title"
        },
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Show Form
### Endpoint
```
GET <BASE_URL>/form/<id>
```
### Response
```
{
    "data": {
        "description": "**description",
        "fields": [
            {
                "form_id": **form_id,
                "id": **field_id,
                "label": "**label_or_question",
                "options": [
                    {
                        "field_id": **field_id,
                        "id": **option_id,
                        "value": "**value_or_answer"
                    }
                ]
            }
        ],
        "id": **form_id,
        "title": "**title"
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Create Form
### Endpoint
```
POST <BASE_URL>/form/
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "title": "<TITLE>",
    "description": "<DESCRIPTION>"
}
```
### Response
```
{
    "data": {
        "description": "**description",
        "fields": [],
        "id": **form_id,
        "title": "**title"
    },
    "message": "Form successfully created.",
    "status": true
}
```

## Edit Form
### Endpoint
```
PUT <BASE_URL>/form/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "title": "<TITLE>",
    "description": "<DESCRIPTION>"
}
```
### Response
```
{
    "data": {
        "description": "**description",
        "fields": [],
        "id": **form_id,
        "title": "**title"
    },
    "message": "Form successfully updated.",
    "status": true
}
```

## Delete Form
### Endpoint
```
DELETE <BASE_URL>/form/
```
### Response
```
{
    "data": {
        "description": "**description",
        "fields": [],
        "id": **form_id,
        "title": "**title"
    },
    "message": "Form successfully deleted.",
    "status": true
}
```

## Show Field
### Endpoint
```
GET <BASE_URL>/form/field/<id>
```
### Response
```
{
    "data": {
        "form_id": **form_id,
        "id": **field_id,
        "label": "**field_or_question",
        "options": []
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Create Field
### Endpoint
```
POST <BASE_URL>/form/field
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "label": "<LABEL>",
    "form_id": <FORM_ID>
}
```
### Response
```
{
    "data": {
        "form_id": **form_id,
        "id": **field_id,
        "label": "**field_or_question",
        "options": []
    },
    "message": "Field successfully created.",
    "status": true
}
```

## Edit Field
### Endpoint
```
PUT <BASE_URL>/form/field/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "label": "<LABEL>",
    "form_id": <FORM_ID>
}
```
### Response
```
{
    "data": {
        "form_id": **form_id,
        "id": **field_id,
        "label": "**field_or_question",
        "options": []
    },
    "message": "Field successfully updated.",
    "status": true
}
```

## Delete Field
### Endpoint
```
DELETE <BASE_URL>/form/field/<id>
```
### Response
```
{
    "data": {
        "form_id": **form_id,
        "id": **field_id,
        "label": "**field_or_question",
        "options": []
    },
    "message": "Field successfully destroyed.",
    "status": true
}
```

## Show Option
### Endpoint
```
GET <BASE_URL>/form/field/option/<id>
```
### Response
```
{
    "data": {
        "field_id": **field_id,
        "id": **option_id,
        "value": "**value_or_answer"
    },
    "message": "Data loaded successfully.",
    "status": true
}
```

## Create Option
### Endpoint
```
POST <BASE_URL>/form/field/option
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "value": "<value>",
    "field_id": <field_id>
}
```
### Response
```
{
    "data": {
        "field_id": **field_id,
        "id": **option_id,
        "value": "**value_or_answer"
    },
    "message": "Option successfully created.",
    "status": true
}
```

## Edit Option
### Endpoint
```
PUT <BASE_URL>/form/field/option/<id>
```
### Headers
```
Content-Type:application/json
```
### Request
```
{
    "value": "<value>",
    "field_id": <field_id>
}
```
### Response
```
{
    "data": {
        "field_id": **field_id,
        "id": **option_id,
        "value": "**value_or_answer"
    },
    "message": "Option successfully updated.",
    "status": true
}
```

## Delete Option
### Endpoint
```
DELETE <BASE_URL>/form/field/option/<id>
```
### Response
```
{
    "data": {
        "field_id": **field_id,
        "id": **option_id,
        "value": "**value_or_answer"
    },
    "message": "Option successfully destroyed.",
    "status": true
}
```

## Show All Response
### Endpoint
```
GET <BASE_URL>/form/response
```
### Response
```
{
    "data": [
        {
            "id": **response_id,
            "user_id": {
                "id": **user_id,
                "name": "**user_name"
            },
            "form_id": {
                "id": **form_id,
                "title": "**form_title"
            },
            "field_id": {
                "id": **field_id,
                "label": "**field_label"
            },
            "option_id": {
                "id": **option_id,
                "value": "**option_value"
            },
            "created_at": "Sun, 28 May 2023 22:51:06 GMT",
        }
    ],
    "message": "Data loaded successfully.",
    "status": true
}
```

## Create Response
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
    "user_id": <user_id>,
    "form_id": <form_id>,
    "field_id": <field_id>,
    "option_id": <option_id>
}
```
### Response
```
{
    "data": {
        "id": **response_id,
        "user_id": {
            "id": **user_id,
            "name": "**user_name"
        },
        "form_id": {
            "id": **form_id,
            "title": "**form_title"
        },
        "field_id": {
            "id": **field_id,
            "label": "**field_label"
        },
        "option_id": {
            "id": **option_id,
            "value": "**option_value"
        },
        "created_at": "Sun, 28 May 2023 22:51:06 GMT",
    },
    "message": "Response successfully created.",
    "status": true
}
```