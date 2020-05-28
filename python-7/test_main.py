import pytest

from requests.exceptions import RequestException, Timeout, TooManyRedirects
from unittest import TestCase
from unittest.mock import Mock, patch

from main import get_temperature


LAT = -14.235004
LNG = -51.92528


@patch('main.requests')
def test_get_temperature_by_lat_lng(mock_requests):
    response = Mock()
    response.json.return_value = {'currently': {'temperature': 62}}
    mock_requests.get.return_value = response
    expected = 16
    assert get_temperature(LAT, LNG) == expected


@patch('main.requests')
def test_get_temperature_zero_degree(mock_requests):
    response = Mock()
    response.json.return_value = {'currently': {'temperature': 0}}
    mock_requests.get.return_value = response
    expected = -17
    assert get_temperature(LAT, LNG) == expected


@patch('main.requests')
def test_get_temperature_json_without_currently_field(mock_requests):
    response = Mock()
    response.json.return_value = {'other': {'temperature': 0}}
    mock_requests.get.return_value = response

    assert get_temperature(LAT, LNG) is None


@patch('main.requests')
def test_get_temperature_json_without_temperature_field(mock_requests):
    response = Mock()
    response.json.return_value = {'currently': {'other': "not temp"}}
    mock_requests.get.return_value = response

    assert get_temperature(LAT, LNG) is None


@patch('main.requests')
def test_get_temperature_invalid_lat(mock_requests):
    response = Mock()
    response.json.return_value = {
        "code": 400,
        "error": "The given location is invalid."
    }
    mock_requests.get.return_value = response
    # The valid range of latitude is -90 and +90
    invalid_lat = 100.487639
    assert get_temperature(invalid_lat, LNG) is None


@patch('main.requests')
def test_get_temperature_invalid_lng(mock_requests):
    response = Mock()
    response.json.return_value = {
        "code": 400,
        "error": "The given location is invalid."
    }
    mock_requests.get.return_value = response
    # The valid range of latitude is -180 and +180
    invalid_lng = 200.856727
    assert get_temperature(LAT, invalid_lng) is None


@patch('main.requests')
def test_get_temperature_connection_error_exception(mock_requests):
    mock_requests.get.side_effect = ConnectionError

    with pytest.raises(ConnectionError):
        get_temperature(LAT, LNG)


@patch('main.requests')
def test_get_temperature_requests_timeout_exception(mock_requests):
    mock_requests.get.side_effect = Timeout

    with pytest.raises(RequestException):
        get_temperature(LAT, LNG)


@patch('main.requests')
def test_get_temperature_requests_too_many_redirects_exception(mock_requests):
    mock_requests.get.side_effect = TooManyRedirects

    with pytest.raises(RequestException):
        get_temperature(LAT, LNG)
