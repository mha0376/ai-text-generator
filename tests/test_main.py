import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_index():
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Text Generator" in response.text

def test_generate_text_story():
    response = client.post("/generate", json={"prompt": "Test prompt", "max_tokens": 50, "output_type": "story"})
    assert response.status_code == 200
    assert "response" in response.json() or "error" in response.json()

def test_generate_text_summary():
    response = client.post("/generate", json={"prompt": "Test prompt", "max_tokens": 50, "output_type": "summary"})
    assert response.status_code == 200
    assert "response" in response.json() or "error" in response.json()

def test_generate_text_analysis():
    response = client.post("/generate", json={"prompt": "Test prompt", "max_tokens": 50, "output_type": "analysis"})
    assert response.status_code == 200
    assert "response" in response.json() or "error" in response.json()