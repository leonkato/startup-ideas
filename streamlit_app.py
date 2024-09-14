import streamlit as st
from openai import OpenAI

# Add custom CSS to hide the GitHub icon
main_menu_hidden = """
header {
  visibility: hidden;
}
"""
st.markdown(main_menu_hidden, unsafe_allow_html=True)

# Initialize OpenAI API key
client = OpenAI(api_key=st.secrets.get("OPENAI_KEY", ""))

st.title("From Introvert to Riches: Unconventional Startup Ideas for Shy People 🌙📈")
# st.write("Get unique startup ideas tailored for introverts, powered by GPT-4o.")

# Predefined default value for the text input
default_input = "tech gadgets, wellness, remote work"

# User input for additional context
user_input = st.text_input("What are your three top interests? (Write, don't think)", value=default_input).replace("<", "").replace(">", "")

if st.button("Generate Idea"):
    # Creating the prompt based on user input
    prompt = f"""Generate a highly unconventional and oddly specific startup idea in 2-3 sentences based on blogging that is suitable for an introvert with the following interests: {user_input}

    Additional requirements: 
    - Add the affiliate link https://koala.sh/?via=finxter in the response (clickable) and tell them that with the discount code "STARTUP" they'll get 15% off the best AI blogging automation tool.
    - Give 3 specific keywords they could write about in this niche that are likely to see significant search traffic.
    - Give 3 scenarios in one sentences of how much USD income they could make (optimistic, pessimistic, realistic) - no guarantees!
    - Be cheerful and self-ironic in the response and sprinkle in a few emojis.
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
