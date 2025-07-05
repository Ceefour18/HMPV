import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to get the response from the model
def get_hmpv_chat(user_input):
    response = client.chat_completions.create(
        model="ft:gpt-3.5-turbo-0125:ceefor-analytics-hub:hmpv-chatbox:BEyqJyv0",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

# Streamlit app
def main():
    st.title("HMPV Chatbox")
    user_input = st.text_input("Enter your message:")
    
    if st.button("Send"):
        if user_input:
            response = get_hmpv_chat(user_input)
            st.write("Bot:", response)
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()