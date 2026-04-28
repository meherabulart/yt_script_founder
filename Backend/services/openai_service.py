from google import genai

# Yahan single/double quotes ke andar apni PURI Gemini API key daalo
client = genai.Client(api_key="AIzaSyAMuX3-YUBq9oyPgPsi7XGBUScEgn2xric")

def generate_script(topic):
    try:
        # Hum latest SDK ka code use kar rahe hain
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=f"Write a highly engaging, viral YouTube script about: '{topic}'. Keep the language simple and engaging (like Hinglish). Include a Hook, Intro, Main Content (with 3 points), and Conclusion. Format it nicely."
        )
        return response.text
    except Exception as e:
        return f"Error aagaya bhai: {str(e)}"