import streamlit as st
from openai import OpenAI
import os

# Initialize AI Client
ai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title("✈️ Our Family Trip Planner")

# Create simple tabs for your features
tab1, tab2, tab3 = st.tabs(["Brainstorming", "AI Itinerary", "Expenses"])

with tab1:
    st.header("Drop your trip ideas here!")
    user_idea = st.text_input("What do you want to do or see?")
    if st.button("Add to Shared List"):
        # 1. Here you would save 'user_idea' to Supabase
        st.success(f"Added: '{user_idea}' to the group list!")

with tab2:
    st.header("AI Generated Itinerary")
    if st.button("🔮 Ask AI to Organize Our Ideas"):
        # 2. Here you would pull all ideas from Supabase and pass them to OpenAI
        st.write("AI is thinking... (This is where your ingestion prompt runs!)")
