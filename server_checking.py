import requests

# 🔑 PASTE YOUR KEY HERE
API_KEY = "AIzaSyCQov-AMS40iwXGlEWCmFtKMwWok7TUdGM"

# The "List Models" Endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    models = response.json()
    print("✅ AVAILABLE MODELS:")
    for model in models['models']:
        # We only want models that support "generateContent" (Chat)
        if "generateContent" in model['supportedGenerationMethods']:
            print(f"- {model['name']}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
