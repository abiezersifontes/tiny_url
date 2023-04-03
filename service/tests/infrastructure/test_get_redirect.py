def test_get_redirect(client):
    response1 = client.post(
        url='/url',
        json={
            "url": "http://www.google.com"
        }
    )
    response = client.get(
        url=f"/url/{response1.json().get('tiny_url').split('/')[4]}",
        follow_redirects=False
    )
    assert response.status_code == 307
