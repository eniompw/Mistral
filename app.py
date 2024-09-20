import requests
import os

url = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("MISTRAL_API_KEY"))}
query = "Which nummber is bigger: 9.11 or 9.9?"
data = {"messages": [{"role": "user", "content": query}], "model": "mistral-large-latest"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])