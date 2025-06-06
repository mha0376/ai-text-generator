from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def generate_text(prompt: str, max_tokens: int, output_type: str) -> str:
    try:
        print(f"Received prompt: {prompt}, max_tokens: {max_tokens}, output_type: {output_type}")
        
        # Prompt Engineering: تعریف پرامپت‌های ساختارمند بر اساس نوع خروجی
        if output_type == "story":
            engineered_prompt = f"""
            You are a creative writer. Write a short story based on the following prompt: "{prompt}".
            Follow these steps:
            1. Create a vivid setting and at least two characters.
            2. Include a clear beginning, middle, and end.
            3. Use descriptive language to engage the reader.
            Ensure the response is in narrative format and under {max_tokens} tokens.
            """
        elif output_type == "summary":
            engineered_prompt = f"""
            You are an expert summarizer. Provide a concise summary of the following prompt: "{prompt}".
            Follow these steps:
            1. Identify the main idea or theme.
            2. Summarize key points in 2-3 sentences.
            3. Use clear and concise language.
            Ensure the response is under {max_tokens} tokens.
            """
        elif output_type == "analysis":
            engineered_prompt = f"""
            You are an analytical AI. Analyze the following prompt: "{prompt}".
            Follow these steps:
            1. Break down the prompt into its core components.
            2. Provide insights or implications of the topic.
            3. Structure the response with an introduction, analysis, and conclusion.
            Ensure the response is under {max_tokens} tokens and formatted as a JSON object:
            ```json
            {{
                "introduction": "...",
                "analysis": "...",
                "conclusion": "..."
            }}
            """
        else:
            raise ValueError("Invalid output_type. Choose 'story', 'summary', or 'analysis'.")

        print(f"Engineered prompt: {engineered_prompt}")
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": engineered_prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        
        print(f"Raw API response: {response}")
        if not response.choices or not response.choices[0].message.content:
            print("Warning: Empty or invalid response from OpenAI API")
            return "No response received from API"
        
        response_text = response.choices[0].message.content.strip()
        print(f"Returning response: {response_text}")
        
        # برای نوع خروجی analysis، مطمئن شوید پاسخ JSON معتبر است
        if output_type == "analysis":
            try:
                json.loads(response_text)
            except json.JSONDecodeError:
                print("Warning: Invalid JSON format for analysis output")
                return "Invalid JSON format received for analysis"
        
        return response_text
    except Exception as e:
        print(f"Error in generate_text: {str(e)}")
        raise Exception(f"Error calling OpenAI API: {str(e)}")