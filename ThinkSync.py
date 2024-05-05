from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as ggi

# Load API key from environment variable
load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")

# Configure Gemini Pro model
ggi.configure(api_key=fetched_api_key)
model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat()

# Dictionary mapping language codes to flag emojis
LANGUAGE_FLAG_DICTIONARY = {
    "af": "🇿🇦",  # Afrikaans
    "ar": "🇸🇦",  # Arabic
    "be": "🇧🇾",  # Belarusian
    "bg": "🇧🇬",  # Bulgarian
    "bn": "🇧🇩",  # Bengali
    "ca": "🇦🇩",  # Catalan
    "cs": "🇨🇿",  # Czech
    "da": "🇩🇰",  # Danish
    "de": "🇩🇪",  # German
    "el": "🇬🇷",  # Greek
    "en": "🇬🇧",  # English
    "es": "🇪🇸",  # Spanish
    "et": "🇪🇪",  # Estonian
    "eu": "🇪🇺",  # European Union
    "fa": "🇮🇷",  # Persian
    "fi": "🇫🇮",  # Finnish
    "fr": "🇫🇷",  # French
    "ga": "🇮🇪",  # Irish
    "gl": "🇪🇸",  # Galician
    "he": "🇮🇱",  # Hebrew
    "hi": "🇮🇳",  # Hindi
    "hr": "🇭🇷",  # Croatian
    "hu": "🇭🇺",  # Hungarian
    "hy": "🇦🇲",  # Armenian
    "id": "🇮🇩",  # Indonesian
    "is": "🇮🇸",  # Icelandic
    "it": "🇮🇹",  # Italian
    "ja": "🇯🇵",  # Japanese
    "ka": "🇬🇪",  # Georgian
    "kk": "🇰🇿",  # Kazakh
    "ko": "🇰🇷",  # Korean
    "lt": "🇱🇹",  # Lithuanian
    "lv": "🇱🇻",  # Latvian
    "mk": "🇲🇰",  # Macedonian
    "mn": "🇲🇳",  # Mongolian
    "ms": "🇲🇾",  # Malay
    "nl": "🇳🇱",  # Dutch
    "no": "🇳🇴",  # Norwegian
    "pl": "🇵🇱",  # Polish
    "pt": "🇵🇹",  # Portuguese
    "ro": "🇷🇴",  # Romanian
    "ru": "🇷🇺",  # Russian
    "si": "🇱🇰",  # Sinhala
    "sk": "🇸🇰",  # Slovak
    "sl": "🇸🇮",  # Slovenian
    "sq": "🇦🇱",  # Albanian
    "sr": "🇷🇸",  # Serbian
    "sv": "🇸🇪",  # Swedish
    "sw": "🇹🇿",  # Swahili
    "ta": "🇮🇳",  # Tamil
    "te": "🇮🇳",  # Telugu
    "th": "🇹🇭",  # Thai
    "tl": "🇵🇭",  # Tagalog
    "tr": "🇹🇷",  # Turkish
    "uk": "🇺🇦",  # Ukrainian
    "ur": "🇵🇰",  # Urdu
    "uz": "🇺🇿",  # Uzbek
    "vi": "🇻🇳",  # Vietnamese
    "zh": "🇨🇳",  # Chinese
    "zu": "🇿🇦",  # Zulu
}

st.title("ThinkSync 🪄")
# st.image(r"C:\Users\ABHISHEKXD\Downloads\Chain-lit\MML-LLM\assets\black-wolf-red-eyes.png")
# Layout with image and content side by side
col1, col2 = st.columns([1, 3])  # Adjust the width ratio as needed

# Add image to the sidebar
col1.image(r"C:\Users\ABHISHEKXD\Downloads\Chain-lit\MML-LLM\assets\aijso.png")

# Content in the main column
with col2:
    st.markdown("""
    ## Welcome to Abhishek - Project 
    - Your Premier AI Chat Service 🤖🌟

    Our service revolutionizes the way you interact with AI, offering an unparalleled experience in conversational AI technology. With Thinksync you can engage in natural language conversations, ask questions, and receive intelligent responses in real-time, all powered by the state-of-the-art Gemini Pro model developed by Google.""")

    

# Add image to the sidebar
with st.sidebar:
    st.title("🔮ThinkSync")
    st.subheader("About - ThinkSync")
    st.markdown("""ThinkSync is a conversational AI platform powered by Streamlit and integrated with Google's Gemini API to provide advanced natural language processing capabilities. It allows users to engage in intelligent conversations and search for information within their uploaded PDF and Word documents.
                With ThinkSync, you can easily upload your documents and ask questions related to the content. The AI model, based on Google's Gemini API, comprehends the context of your queries and generates insightful responses based on the document's content. Whether you're exploring complex topics, conducting research, or seeking answers from your data, ThinkSync provides an intuitive interface for interactive exploration.
                Utilizing Streamlit's user-friendly interface, ThinkSync offers a seamless experience for users to interact with the AI model.""")
    st.subheader("Connect with Me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)")
    st.markdown("[Twitter](https://twitter.com/your-twitter-handle)")
    st.markdown("[GitHub](https://github.com/your-github-profile)")

st.success("You are Connected ", icon="💚")
st.sidebar.image(r"C:\Users\ABHISHEKXD\Downloads\Chain-lit\MML-LLM\assets\picofme (1).png")

# Language selection
selected_language = st.sidebar.selectbox("Select Response Language", list(LANGUAGE_FLAG_DICTIONARY.keys()))

user_quest = st.text_input("Ask a question:")
btn=st.button("Submit✅")

if btn and user_quest:
    response = chat.send_message(f"[{selected_language}] {user_quest}", stream=True)
    # Display response
    if response:
        st.subheader("Response : ")
        for word in response:
            st.text(word.text)
            
with st.expander("Additional Details and Steps to Follow"):
    st.write("""
    **Additional Details:**
    - This application allows you to engage in conversations directly with the Gemini Pro model, a state-of-the-art language generation AI developed by Google.
    - You can ask questions, discuss various topics, or simply engage in casual conversation with the model.
    - Experience the power of conversational AI and explore the capabilities of the Gemini Pro model in real-time.

    **Steps to Follow:**
    1. Enter your question or topic of interest in the text input field.
    2. Click the "Ask" button to send your query to the Gemini Pro model.
    3. The model will generate a response based on the input provided and deliver it instantly.
    4. Engage in meaningful conversations, explore diverse topics, and experience the future of AI-driven interaction.
    """)


# Copyright notice
st.markdown("<div style='text-align: center;'><p>© 2024 Abhishek - Mishra. All rights reserved.</p></div>", unsafe_allow_html=True)

