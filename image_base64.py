import base64
import requests
import os

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

image_path = "image.png"
base64_image = encode_image(image_path)

url = "https://api.mistral.ai/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("MISTRAL_API_KEY"))}
text = {"type": "text", "text": "What's in this image?"}
content = [text, {"type": "image_url", "image_url":  f"data:image/jpeg;base64,{base64_image}"}]
data = {"messages": [{"role": "user", "content": content}], "model": "pixtral-12b-2409"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])