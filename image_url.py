import requests
import os

url = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("MISTRAL_API_KEY"))}
text = {"type": "text", "text": "What's in this image?"}
image_url = "https://tripfixers.com/wp-content/uploads/2019/11/eiffel-tower-with-snow.jpeg"
content = [text, {"type": "image_url", "image_url": image_url}]
data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])