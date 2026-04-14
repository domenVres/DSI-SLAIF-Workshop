from openai import OpenAI


API_KEY = "GaMS-server-key"
BASE_URL = "http://localhost:8001/v1"


def get_client():
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL
    )

    return client


def test_prompt(prompt, client, model):
    messages = [
        {"role": "user", "content": prompt},
    ]

    completion_kwargs = {
        "model": model,
        "messages": messages,
        "max_completion_tokens": 10
    }
    
    try:
        response = client.chat.completions.create(**completion_kwargs)
        content = response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return

    print("-" * 30)
    print("Uporabnik:", prompt)
    print()
    print("Asistent:", content)
    print("-" * 30)
        

if __name__ == "__main__":
    client = get_client()
    prompt = "Napiši 'Zdravo' nazaj"
    model = "/models/GaMS3-12B-Instruct"
    test_prompt(prompt, client, model)
