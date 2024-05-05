import streamlit as st
import os
from dotenv import load_dotenv
import tempfile
from PyPDF2 import PdfReader
from docx import Document
import google.generativeai as ggi

# Load API key from environment variable
load_dotenv(".env")
fetched_api_key = os.getenv("API_KEY")

# Configure Gemini Pro model
try:
    ggi.configure(api_key=fetched_api_key)
    model = ggi.GenerativeModel("gemini-pro") 
    chat = model.start_chat()
except Exception as e:
    st.error(f"Failed to initialize the Gemini Pro model: {str(e)}")
    st.stop()

def LLM_Response(question):
    try:
        response = chat.send_message(question)
        return response.text.strip()
    except Exception as e:
        st.error(f"Failed to get response from the Gemini Pro model: {str(e)}")
        return None

def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    text = ""
    with open(temp_file_path, "rb") as f:
        pdf_reader = PdfReader(f)
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    os.unlink(temp_file_path)  # Remove the temporary file
    return text

def extract_text_from_docx(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    text = ""
    doc = Document(temp_file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    
    os.unlink(temp_file_path)  # Remove the temporary file
    return text

st.title("DataChat 📊💬")
# Sidebar
with st.sidebar:
    st.image(r"C:\Users\ABHISHEKXD\Downloads\Chain-lit\MML-LLM\assets\ai-cloud-with-robot-face.png", width=300)
    st.title("DataChat❤️‍🔥👻")
    st.subheader("About {|}")
    st.write("""
    DataChat revolutionizes the way you explore and interact with your own data. Our service allows you to have meaningful conversations, ask questions, and receive insightful responses, all within the context of your uploaded PDF and Word documents.
    
    With DataChat, you can harness the power of conversational AI to unlock hidden insights, analyze complex information, and make informed decisions. Powered by the advanced Gemini Pro model developed by Google, DataChat ensures accuracy, reliability, and speed in processing your queries.
    
    Experience the future of data interaction with DataChat today!
    """)
# Layout with image and content side by side
col1, col2 = st.columns([1, 3])  # Adjust the width ratio as needed

# Add image to the sidebar
col1.image(r"C:\Users\ABHISHEKXD\Downloads\Chain-lit\MML-LLM\assets\2150688377-removebg-preview.png")

# Content in the main column
with col2:
    st.markdown("""
    ## Welcome to DataChat 📊💬 
    - Your Premier AI-Powered Data Chat Service 🤖🌟

    DataChat revolutionizes the way you explore and interact with your own data. Our service allows you to have meaningful conversations, ask questions, and receive insightful responses, all within the context of your uploaded PDF and Word documents.

    With DataChat, you can harness the power of conversational AI to unlock hidden insights, analyze complex information, and make informed decisions. Powered by the advanced Gemini Pro model developed by Google, DataChat ensures accuracy, reliability, and speed in processing your queries.

    - Experience the future of data interaction with DataChat today!
    """)



# File upload component
uploaded_file = st.file_uploader("Upload PDF or Word file", type=["pdf", "docx"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        text_content = extract_text_from_pdf(uploaded_file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text_content = extract_text_from_docx(uploaded_file)
    
    st.subheader("Extracted Text:")
    st.text_area("Text Content", text_content)

    user_quest = st.text_input("Ask a question:")
    btn = st.button("Ask")

    if btn and user_quest:
        result = LLM_Response(user_quest)
        if result:
            st.subheader("Response : ")
            st.text(result)

# Additional details and steps to follow
with st.expander("Additional Details and Steps to Follow"):
    st.write("""
    **Additional Details:**
    - This application allows you to chat with the Gemini Pro model using your own PDF or Word documents.
    - Simply upload your document, ask a question, and the model will respond based on the content of your document.

    **Steps to Follow:**
    1. Upload a PDF or Word document using the file uploader.
    2. Once the text content is extracted, you can ask questions related to the content.
    3. Click the "Ask" button to send your question to the Gemini Pro model.
    4. The model will respond with an answer based on the content of your document.
    """)

# Copyright notice
st.markdown("<div style='text-align: center;'><p>© 2024 Shinchan. All rights reserved.</p></div>", unsafe_allow_html=True)
