from google import genai

client = genai.Client(
    api_key="AIzaSyDxagBAy8vPjbzAta01hfwKHV2k_ZEQlNw"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)