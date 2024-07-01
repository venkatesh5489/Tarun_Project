import pytest
import requests

# Define API base URL (update with your local server URL)
BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module")
def api_url():
    return BASE_URL

def test_get_raw_stock_data(api_url):
    response = requests.get(f"{api_url}/raw_data/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    # Add more assertions as needed to validate the response format and data

def test_get_financial_metrics(api_url):
    response = requests.get(f"{api_url}/financial_metrics/")
    assert response.status_code == 200
    assert len(response.json()) > 0
    # Add more assertions as needed to validate the response format and data

# You can add more tests for specific edge cases or additional endpoints here
