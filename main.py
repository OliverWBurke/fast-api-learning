from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get(path="/")
async def root():
    """
    Hello world message at root of API
    """
    return {"Hello": "World"}


@app.get(path="/health")
async def health():
    """
    This is a health endpoint. This is just used to ensure that the App is up and healthy

    :return: status of the app
    """
    return {"status": "OK"}


@app.get(path="/unhealth")
async def unhealth():
    """
    This will always return a 502 error by design
    """
    return HTTPException(
        status_code=502, detail="Unhealth endpoint always returns a 502"
    )


@app.post(path="/message/{message}")
async def post_message(message: str):
    """
    This just sends back the message that is sent to the endpoint

    :param message:
    :return:
    """
    return {"message_received": message}
