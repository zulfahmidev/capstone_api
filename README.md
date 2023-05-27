# HOW TO USE API

## API FOR REGISTER AKUN
```http

POST <URL>/auth/register

# Headers
    Content-Type:application/json

# Example Body
Body:
{
    "name": "<NAME>",
    "email": "<EMAIL>",
    "password": "<PASSWORD>",
    "phone": "<NO HP>",
    "address": "<ADDRESS>",
    "birth_date": "<y-m-d>"
}

#Response
{
    "message": "Registration successful! Please check your mailbox for email verification",
    "success": true
}

```
## you can check email for verification your email
### Example email verification
![image](https://github.com/zulfahmidev/capstone_api/assets/109580466/8936f40f-4911-48f3-b702-40fd1465d7d2)


## API FOR LOGIN AKUN

```http

POST <URL>/auth/login
# Headers
    Content-Type:application/json
    
#Example Body
Body:
{
    "email":"<EMAIL>",
    "password":<PASSWORD>
}

#Response
{
    "message": "Your have succesfully logged in.",
    "status": true
}
```

## API FOR SHOW DATA AKUN
```http
GET <URL>/auth/me
#reponse
{
    "msg": "DATA AKUN"
}
```

## API FOR FORGOT PASSWORD

```http
POST <URL>/auth/forgot-password

# Headers
    Content-Type:application/json

#Example Body
Body:
{
    "email": "<EMAIL>"
}

#Response
{
    "body": {
        "reset_token": "900a3963e2b5a06f11988f5db15dcbe0"
    },
    "message": "Token reset has been successfully generated.",
    "status": true
}
```

## API FOR RESET PASSWORD

```http
POST <URL>/auth/reset-password/<token>

# Headers
    Content-Type:application/json

#Example Body
Body:
{
    "password": "<NEW PASSWORD>"
}

#Response
{
    "message": "Password successfully changed.",
    "status": true
}
```
