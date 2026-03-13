from api_health_test import query_llm

def test_consistency():

    prompt = "Explain what malware is in one sentence."

    responses = []

    for i in range(3):
        responses.append(query_llm(prompt))

    print("Responses:")

    for r in responses:
        print(r)


if __name__ == "__main__":
    test_consistency()
