from fastapi.testclient import TestClient
from roiapi.main import app

client = TestClient(app)


def test_generate_valid() -> None:
    response = client.post("/generate", json={"prompt": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert "Hello" in data["response"]


def test_generate_empty() -> None:
    response = client.post("/generate", json={"prompt": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Prompt cannot be empty."


def test_specific_input() -> None:
    response = client.post("/generate", json={"prompt": "Hello, who are you?"})
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["response"] == "LLM says: I am me"
