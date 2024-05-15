from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_read_users_sync():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

    
@pytest.mark.asyncio
async def test_read_users_async():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

