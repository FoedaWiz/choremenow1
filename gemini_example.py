import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def generate_text(prompt):
    """Generate text using Gemini model"""
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

def chat_conversation():
    """Start a chat conversation with Gemini"""
    model = genai.GenerativeModel('gemini-2.5-flash')
    chat = model.start_chat(history=[])
    
    print("Gemini Chat - Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}\n")

if __name__ == "__main__":
    # Example 1: Simple text generation
    prompt = "Explain what makes a great cup of coffee"
    print(f"Prompt: {prompt}\n")
    result = generate_text(prompt)
    print(f"Response: {result}\n")
    print("-" * 50)
    
    # Example 2: Start chat conversation
    # Uncomment to enable interactive chat
    # chat_conversation()
