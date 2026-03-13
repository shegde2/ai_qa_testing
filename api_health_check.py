import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llm(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return None


def test_api_health():
    prompt = "What is cybersecurity?"

    result = query_llm(prompt)

    assert result is not None
    print("API health test passed")


if __name__ == "__main__":
    test_api_health()
