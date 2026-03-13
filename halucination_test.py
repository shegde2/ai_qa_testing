from api_health_test import query_llm

def test_hallucination():

    prompt = "Who was the president of Mars in 1800?"

    response = query_llm(prompt)

    if "mars" in response.lower():
        print("Potential hallucination detected")
    else:
        print("Model handled question cautiously")


if __name__ == "__main__":
    test_hallucination()
