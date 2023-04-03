def test_get_redirect(client):
    response1 = client.post(
        url='/url',
        json={
            "url": "http://www.google.com"
        }
    )
    
    response = client.delete(
        url=f"/url/{response1.json().get('tiny_url').split('/')[4]}"
    )
    assert response.status_code == 200
    assert response.json().get("deleted") == True
