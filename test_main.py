import json

from fastapi.testclient import TestClient

from backend.app.api import YesNo, app

client = TestClient(app)


def test_main_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_main_root_post():
    response = client.post("/")
    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_app_details():
    assert client.app.title == "Fast API Learning"
    assert client.app.version == "0.0.1"
    contacts = client.app.contact
    assert contacts.get("name")
    assert contacts.get("url")
    assert contacts.get("email")


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_unhealth():
    response = client.get("/unhealth")
    assert response.status_code == 502
    assert response.json() == {"detail": "Unhealth endpoint always returns a 502"}


def test_post_message():
    test_message = "test msg"
    response = client.post(f"/message/{test_message}")
    assert response.status_code == 200
    assert response.json() == {"message_received": test_message}


def test_post_too_long_message():
    test_message = "test message"
    response = client.post(f"/message/{test_message}")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "ensure this value has at most 10 characters"
    )


def test_post_message_no_message():
    response = client.post("/message/")
    assert response.status_code != 200


def test_post_number():
    test_number = 5
    response = client.post(f"/number/{test_number}")
    assert response.status_code == 200
    assert response.json() == {
        "message": f"you sent the number {test_number}",
        "number": test_number,
    }


def test_post_text_to_number():
    test_number = "five"
    response = client.post(f"/number/{test_number}")
    assert response.status_code == 422
    assert response.reason == "Unprocessable Entity"


def test_yes_no_class():
    yes = YesNo("yes")
    no = YesNo("no")
    assert type(yes) == YesNo
    assert yes.value == "yes"
    assert type(no) == YesNo
    assert no.value == "no"


def test_yes_no():
    yes_response = client.get("/yes_or_no/yes")
    no_response = client.get("/yes_or_no/no")
    assert yes_response.status_code == 200
    assert no_response.status_code == 200
    assert yes_response.json() == {"option_chosen": "yes"}
    assert no_response.json() == {"option_chosen": "no"}


def test_print_word_simple():
    test_word = "test_word"
    test_count = 2
    response = client.get(f"/print_word/?word={test_word}&print_count={test_count}")
    assert response.status_code == 200
    assert response.json()["word"] == f"{test_word},{test_word}"


def test_print_word_upper():
    test_word = "test_word"
    test_count = 2
    response = client.get(
        f"/print_word/?word={test_word}&print_count={test_count}&make_upper=TRUE"
    )
    assert response.status_code == 200
    test_word_upper = test_word.upper()
    assert response.json()["word"] == f"{test_word_upper},{test_word_upper}"


def test_send_body():
    test_body = {
        "test_string": "string",
        "test_integer": 0,
        "test_float": 0,
        "test_bool": True,
    }
    response = client.post("/send_body/", data=json.dumps(test_body))
    assert response.status_code == 200
    response_json = response.json()
    for k, v in test_body.items():
        assert response_json[k] == v
    assert response_json["test_optional_with_default"] == "default_value"


def test_send_body_with_raise_requested():
    test_body = {
        "test_string": "string",
        "test_integer": 0,
        "test_float": 0,
        "test_bool": True,
        "test_raising_error": True,
    }
    response = client.post("/send_body/", data=json.dumps(test_body))
    assert response.status_code == 404
    assert response.json()["detail"] == "Raising an error cos you asked it to"


def test_send_body_with_formatted_response():
    test_body = {
        "test_string": "string",
        "test_integer": 0,
        "test_float": 0,
        "test_bool": True,
        "test_format_output": True,
    }
    response = client.post("/send_body/", data=json.dumps(test_body))
    assert response.status_code == 200
    assert response.json()["your_request_body_formatted"]
