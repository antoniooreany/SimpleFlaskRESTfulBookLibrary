def test_login_successful(client):
    response = client.post('/login', json={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert response.json['message'] == "Login successful"

def test_login_failed_invalid_credentials(client):
    response = client.post('/login', json={"username": "admin", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json['error'] == "Invalid credentials"

def test_login_failed_missing_username(client):
    response = client.post('/login', json={"password": "password"})
    assert response.status_code == 401
    assert response.json['error'] == "Invalid credentials"

def test_login_failed_missing_password(client):
    response = client.post('/login', json={"username": "admin"})
    assert response.status_code == 401
    assert response.json['error'] == "Invalid credentials"

def test_logout_successful(client):
    response = client.post('/logout', json={"username": "admin"})
    assert response.status_code == 200
    assert response.json['message'] == "Logout successful"

def test_logout_failed_missing_username(client):
    response = client.post('/logout', json={})
    assert response.status_code == 200
    assert response.json['message'] == "Logout successful"