# fast-api-learning
Repo for things that I'm playing with to learn FastAPI

## API Endpoints

Have implemented some basic endpoints

### GET Root
There is a root endpoint, that just returns a hello world type response.

### GET Health
There is a health endpoint. This is just here to allow checking that the API
is up and running, and should always just return a status:OK message.

### GET Unhealth
This endpoint will always return a 502 status code. Just implemented this to
try out raising HTTP exception codes.

### POST Message
This is a post endpoint. It just accepts a message as a path parameter,
and returns the message sent in the response.

### POST Number
This is a post endpoint, that includes a type hint. The endpoint expects to receive
an integer, and just returns the integer that was sent.
It returns the number in a message, as well as the raw value.

Because this has the type hint set up, it will return an error status if a non integer
is provided. This doesn't need any code, it's dealt with by FastAPI.


## API Documentation

### App Description
We can set some metadata in the app when it is created.
This will be shown in the swagger docs. I have completed most of the allowed parameters here,
details of the parameters that can be passed are [here](https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api)

### Endpoint Tags
We can specify tags against each endpoint.
This will group the endpoints in the swagger documentation.

This is done by creating a list of tags, which have a name and description,
and adding that as a parameter when creating the App.

Once the tags are created, they can be associated with the endpoints.
Each endpoint can have more than one tag,
if it makes sense for it to be shown in multiple sections.

### Function Docstrings
Adding docstrings to the functions that are defined as endpoints will mean
that the Swagger docs that are generated will show these docs.
The docstrings should just be plain MD text.

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

There is an alternative docs page that gets created as well,
at http://localhost:8000/redoc


### HTTPie
[HTTPie](https://httpie.io/docs/cli) can be used from the commandline as well. HTTPie can be installed from pip
`pip install httpie`

```commandline
> http GET localhost:8000

HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Sun, 24 Jul 2022 07:22:47 GMT
server: uvicorn

{
    "Hello": "World"
}

> http GET localhost:8000/health

HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Sun, 24 Jul 2022 07:24:24 GMT
server: uvicorn

{
    "status": "OK"
}


> http GET localhost:8000/unhealth

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

> http POST localhost:8000/message/Message_To_Send

HTTP/1.1 200 OK
content-length: 38
content-type: application/json
date: Sun, 24 Jul 2022 07:35:15 GMT
server: uvicorn

{
    "message_received": "Message_To_Send"
}

```
