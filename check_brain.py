import google.generativeai as genai

# Setup
API_KEY = "AIzaSyAnvuxuaMDF6NAVLdiA3JxK9HWaZljXk5g"
genai.configure(api_key=API_KEY)

print("🔍 Contacting Google Server to list available brains...")
print("----------------------------------------------------")

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ FOUND: {m.name}")
except Exception as e:
    print(f"❌ ERROR: {e}")