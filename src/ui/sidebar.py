import streamlit as st
from src.config import Config

def render_sidebar():
    with st.sidebar:
        st.header("Configuration")
        
        # 1. API Key Management
        if Config.API_KEY:
            st.success("API Key Loaded")
            api_key = Config.API_KEY
        else:
            api_key = st.text_input("Enter Gemini API Key", type="password")
            if not api_key:
                st.warning("API Key required")

        st.divider()
        
        # 2. Prompt Management
        st.subheader("Agent Logic")
        st.info("Customize the agent's behavior below.")
        
        prompts = st.session_state.get("prompts", Config.DEFAULT_PROMPTS.copy())
        
        new_prompts = {}
        new_prompts["categorize"] = st.text_area("Categorization Rules", prompts["categorize"], height=100)
        new_prompts["action_item"] = st.text_area("Action Extraction Rules", prompts["action_item"], height=100)
        new_prompts["reply"] = st.text_area("Reply Personality", prompts["reply"], height=100)
        
        if st.button("Save Configuration"):
            st.session_state.prompts = new_prompts
            st.success("Configuration Updated")
            
        return api_key