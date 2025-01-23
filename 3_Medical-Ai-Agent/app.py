import streamlit as st
from dotenv import load_dotenv
import os
import requests
from knowledge_base import scrape_medical_data

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def query_groq_api(prompt, knowledge_base):
    """
    Sends a query to the Groq API to process natural language input.
    Args:
        prompt (str): The user's query.
        knowledge_base (list): List of FAQs for context.
    Returns:
        str: Groq's response.
    """
    url = "https://api.groq.com/query"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {
        "prompt": prompt,
        "context": [{"question": faq["question"], "answer": faq["answer"]} for faq in knowledge_base]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        return f"Error: {response.json().get('error', 'Unknown error')}"
    return response.json().get("response", "No response available")

# Streamlit App
st.title("Medical Center AI Agent")
st.subheader("Ask me anything about the Medical Center!")

# Input URL for scraping
url = st.text_input("Enter the URL to fetch Medical Center data:", placeholder="https://daffodilvarsity.edu.bd/medical/diu-medical-center")

if url:
    try:
        # Scrape data
        with st.spinner("Fetching data..."):
            scraped_data = scrape_medical_data(url)
        
        st.success("Data fetched successfully!")
        st.write("### Knowledge Base Preview")
        for item in scraped_data:
            st.write(f"**Q:** {item['question']}")
            st.write(f"**A:** {item['answer']}")

        # User Query
        user_query = st.text_input("Ask your question:")
        if user_query:
            with st.spinner("Querying Groq API..."):
                response = query_groq_api(user_query, scraped_data)
                st.write("### AI Response")
                st.write(response)

    except Exception as e:
        st.error(f"Error: {e}")
