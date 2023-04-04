from unittest.mock import patch

def test_delete_url(client):
    with patch('service.app.application.service_url.ServiceUrl.delete_url', return_value=True):
        response = client.delete(url="/1234567")
    assert response.status_code == 200
    assert response.json().get("deleted") is True

