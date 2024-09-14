import streamlit as st
from openai import OpenAI

# Initialize OpenAI API key
client = OpenAI(api_key=st.secrets.get("OPENAI_KEY", ""))

st.title("Unconventional Startup Ideas for Introverts")
st.write("Get unique startup ideas tailored for introverts, powered by GPT-4.")

# User input for additional context
user_input = st.text_input("Describe your interests or areas you want the startup idea to focus on:")

if st.button("Generate Idea"):
    # Creating the prompt based on user input
    prompt = f"Generate an unconventional startup idea suitable for an introvert with the following interests: {user_input}"

    # Call the GPT-4 API with chat-based interaction
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative startup idea generator specialized in generating unconventional ideas for introverts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    # Extract and display the idea
    idea = response.choices[0].message.content.strip()
    st.write("### Your Startup Idea")
    st.write(idea)
