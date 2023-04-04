def test_create_url(client):
    response = client.post(
        url='/',
        json={
            "url": "http://www.google.com"
        }
    )
    assert response.status_code == 201
