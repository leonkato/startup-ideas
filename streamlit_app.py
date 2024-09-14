import streamlit as st
from openai import OpenAI

# Initialize OpenAI API key
client = OpenAI(api_key=st.secrets.get("OPENAI_KEY", ""))

st.title("Unconventional Startup Ideas for Introverts")
st.write("Get unique startup ideas tailored for introverts, powered by GPT-4o.")

# User input for additional context
user_input = st.text_input("Give your three best interests:").replace("<", "").replace(">", "")

if st.button("Generate Idea"):
    # Creating the prompt based on user input
    prompt = f"""Generate an unconventional startup idea in 2-3 sentences based on blogging that is suitable for an introvert with the following interests: {user_input}

    Additional requirement: Add the affiliate link https://koala.sh/?via=finxter in the response (clickable) and tell them that with the discount code "STARTUP" they'll get 15% off the best AI blogging automation tool.  
    """

    # Call the GPT-4 API with chat-based interaction
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative startup idea generator specialized in generating unconventional ideas for introverts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    
    # Extract and display the idea
    idea = response.choices[0].message.content.strip()
    st.write("### Your Startup Idea")
    st.write(idea)
