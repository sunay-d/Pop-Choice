import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)

system_prompt = "You are an enthusiastic movie expert who loves recommending movies to people. You will be given two pieces of information - some context about movies and a question. Your main job is to formulate a short answer to the question using the provided context. If you are unsure and cannot find the answer in the context, say that you don't know. Please do not make up the answer. If they greeted you greet them back politely."

def get_chat_completion(question, response_match):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            ),
            contents=f'Context: {response_match} - Question: {question}'
        )

        return response.text
    
    except Exception as e:
        print(e)
        return response_match

