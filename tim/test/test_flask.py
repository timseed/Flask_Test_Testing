import json
from unittest.mock import Mock, patch

import pytest
from requests.models import Response

from tim.controller.app import APP


def test_resp(value: bytes = "", code: int = 200) -> Response:
    the_response = Mock(spec=Response)
    the_response.data = value
    the_response.status_code = code
    return the_response

def test_resp_method():
    good_resp = test_resp(b"Success")
    good_resp2 = test_resp(b"Success")
    assert good_resp.status_code == good_resp2.status_code
    assert good_resp.data == good_resp2.data
    bad_resp  = test_resp(b"Failure",code = 404)
    assert bad_resp.status_code != good_resp2.status_code
    assert bad_resp.status_code == 404

@pytest.fixture
def client():
    """ return a test client """
    client_app = APP.test_client()
    t = type(client_app)
    yield client_app


def test_check_web_is_ok(client):
    """ Web Check """

    rv = client.get('/tim1/top/')
    assert rv is not None
    assert rv.status_code == 200 or 308
    assert b'Running' in rv.data


def test_check_web_is_fail(client):
    """ Web Check """

    rv = client.get('/bad_endpoint')
    assert rv is not None
    assert rv.status_code == 404




def test_check_web_returns_data(client):
    """ Web Check """

    rv = client.get('/tim1/top/')
    assert rv is not None
    assert rv.status_code == 200 or 308
    assert b'Running' in rv.data

    rv = client.get('/tim1/hello/')
    assert rv is not None
    assert rv.status_code == 200 or 308
    assert b'Hello, World' in rv.data




@patch('flask.testing.FlaskClient.get', return_value=test_resp(b'Running'))
def test_fake_mocked_web_returns_data(mock_fun, client):
    """ Web Check
    This Route actually DOES NOT Exists. But I want to ensure we
    can mock fake routes.
    """
    rv = client.get('/fake_route')
    assert rv is not None
    assert rv.status_code == 200 or 308
    assert b'Running' in rv.data


#
# Route with Params testing
#

def test_person_route_exists_this_should_fail(client):
    rv = client.get('/tim1/person/')  # Missing Params on the route

    assert rv is not None
    assert rv.status_code not in [200, 308]
    assert rv.status_code == 404


def test_person_route_exists_this_should_work(client):
    rv = client.get('/tim1/person/bob/number/123')

    assert rv is not None
    assert rv.status_code != 404
    assert rv.status_code in [200, 308]
    jd = json.loads(rv.data)
    assert jd == json.loads("""{"name": "bob", "number": "123", "status": "Ok"}""")

def test_person_route_exists_opt_argument_this_should_work(client):
    rv = client.get('/tim1/person/bob/number/123?address=Test%20Address')
    assert rv is not None
    assert rv.status_code != 404
    assert rv.status_code in [200, 308]
    jd = json.loads(rv.data)
    assert jd == json.loads("""{"name": "bob", "number": "123", "status": "Ok", "address":"Test Address"}""")


addr_str = b"{\"name\": \"bob\", \"number\": \"123\", \"status\": \"Ok\", \"address\":\"Test Address\"}"
@patch('flask.testing.FlaskClient.get', return_value=test_resp(addr_str))
def test_person_patched_opt_argument_this_should_work(mock_fun, client):
    rv = client.get('/tim1/person/bob/number/123?address=Test%20Address')
    assert rv is not None
    assert rv.status_code != 404
    assert rv.status_code in [200, 308]
    jd = json.loads(rv.data)
    assert jd == json.loads(addr_str)


addr_str2 = b"{\"name\": \"bob\", \"number\": \"123\", \"status\": \"Ok\", \"address\":\"Test Address\"}"
@patch('flask.testing.FlaskClient.get', return_value=test_resp(addr_str))
def test_person_patched_opt_argument_this_should_work(mock_fun, client):
    rv = client.get('/tim1/person/bob/number/123?address=')
    assert rv is not None
    assert rv.status_code != 404
    assert rv.status_code in [200, 308]
    jd = json.loads(rv.data)
    assert jd == json.loads(addr_str2)
