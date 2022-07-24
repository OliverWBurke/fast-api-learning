from fastapi import FastAPI, HTTPException

description = """
Fast API Learning

# Overview
This is an API that I am playing with in order to learn FastAPI.
This is not designed to do anthing particularly useful,
I am just trying to implement basic functionality,
"""

tags = [
    {"name": "basic", "description": "These are just basic endpoints"},
    {
        "name": "basic_plus",
        "description": "These are endpoints that have some more functionality",
    },
]

app = FastAPI(
    title="Fast API Learning",
    description=description,
    version="0.0.1",
    contact={
        "name": "Oliver",
        "url": "https://www.oliverburke.uk/",
        "email": "hi@oliverburke.uk",
    },
    openapi_tags=tags,
)


@app.get(path="/", tags=["basic"])
async def root():
    """
    Hello world message at root of API
    """
    return {"Hello": "World"}


@app.get(path="/health", tags=["basic"])
async def health():
    """
    This is a health endpoint. This is just used to ensure that the App is up and healthy

    :return: status of the app
    """
    return {"status": "OK"}


@app.get(path="/unhealth", tags=["basic", "basic_plus"])
async def unhealth():
    """
    This will always return a 502 error by design
    """
    return HTTPException(
        status_code=502, detail="Unhealth endpoint always returns a 502"
    )


@app.post(path="/message/{message}", tags=["basic_plus"])
async def post_message(message: str):
    """
    This just sends back the message that is sent to the endpoint

    :param message:
    :return:
    """
    return {"message_received": message}
