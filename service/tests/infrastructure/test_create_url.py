def test_create_url(client):
    response = client.post(
        url='/url',
        json={
            "url": "http://www.google.com"
        }
    )
    assert response.status_code == 201
