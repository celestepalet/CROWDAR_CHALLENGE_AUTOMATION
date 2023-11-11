from api.request_manager import RequestManager
import pytest
from api.constants import DEPARTMENTS_ENDPOINT


@pytest.mark.api_testing
def test_departments_exist():
    # Perform GET request to the web service
    response = RequestManager().make_request('GET', DEPARTMENTS_ENDPOINT)
    # Verify that the request was successful (response code 200)
    expected_status = 200
    actual_status = response[0]
    assert actual_status == expected_status, "The request to the web service was unsuccessful."
    # Verify that the response body contains departments
    actual_response_body = response[1].json()
    assert "departments" in actual_response_body, "The 'departments' field is not present in the response."
    departments = actual_response_body["departments"]
    assert len(departments) > 0, "The apartment list is empty."
