from unittest.mock import patch

def test_get_redirect(client):
    with patch('service.app.application.service_url.ServiceUrl.get_url', return_value='http://www.google.com'):
        response = client.get(url="/url/123456", follow_redirects=False)
        assert response.status_code == 307
