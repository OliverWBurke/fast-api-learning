# fast-api-learning
Repo for things that I'm playing with to learn FastAPI

## API

Have implemented 4 basic endpoints, three of them are get endpoints, and one is a post.

### Root
There is a root endpoint, that just returns a hello world type response.

### Health
There is a health endpoint. This is just here to allow checking that the API
is up and running, and should always just return a status:OK message.

### Unhealth
This endpoint will always return a 502 status code. Just implemented this to
try out raising HTTP exception codes.

### Post Message
This is the only endpoint that is a post endpoint. It just accepts a message
as a path parameter, and returns the message sent in the response.


## Running

We can serve the API by running this using [uvicorn](https://www.uvicorn.org/)

```commandline
uvicorn main:app --host "0.0.0.0" --port 8000 --reload
```

## Access for Testing

### Browser
Once this is running, this can be accessed via a browser at http://localhost:8000/

### Swagger Docs
Alternatively, FastAPI generates swagger docs at http://localhost:8000/docs,
which can be used to test out the endpoints.

### HTTPie
HTTPie can be used from the commandline as well. HTTPie can be installed from pip
`pip install httpie`

```commandline
> http localhost:8000

HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Sun, 24 Jul 2022 07:22:47 GMT
server: uvicorn

{
    "Hello": "World"
}

> http localhost:8000/health

HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Sun, 24 Jul 2022 07:24:24 GMT
server: uvicorn

{
    "status": "OK"
}


> http localhost:8000/unhealth

HTTP/1.1 200 OK
content-length: 84
content-type: application/json
date: Sun, 24 Jul 2022 07:24:35 GMT
server: uvicorn

{
    "detail": "Unhealth endpoint always returns a 502",
    "headers": null,
    "status_code": 502
}



```
