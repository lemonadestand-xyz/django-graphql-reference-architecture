# Here are a list of quick graphql calls and their output


## Get an Auth Token
```
mutation{
  tokenAuth(username: "+17654907385", password: "320464") {
    token
  }
}
```

### Response
```
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cCI6MTU5OTU5ODcwMiwib3JpZ0lhdCI6MTU5OTU5ODQwMn0.yPzf26LryOp9Dp7c4bGU3x-KXFbry2-xLgpj98h4rro"
    }
  }
}
```

#### Add this to your `REQUEST HEADERS`
Take the "token" returned from the `tokenAuth` response and add it to the "REQUEST HEADERS" in `graphql` URL endpoint
```
{
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cCI6MTU5OTU5Mjg0MSwib3JpZ0lhdCI6MTU5OTU5MjU0MX0.WDnSvXmvvGpQfBgZqwdXxaFty9FioMp6suJrjiYkQYY"
}
```


## Get Users Profile
```
{
  profile {
    user {
      firstName
      lastName
      email
    }
    city
    state
    country
  }
}
```

### Response
```
{
  "data": {
    "profile": {
      "user": {
        "firstName": "",
        "lastName": "",
        "email": "demo.user@gmail.com"
      },
      "city": "Kokomo",
      "state": "INDIANA",
      "country": "US"
    }
  }
}
```