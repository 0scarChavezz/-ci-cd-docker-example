import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hola" in response.data

def test_suma_route():
    client = app.test_client()
    response = client.get('/api/suma')
    assert response.status_code == 200  
    data = response.get_json()
    assert data["resultado"] == 10

