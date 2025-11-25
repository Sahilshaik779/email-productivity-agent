import streamlit as st
from src.config import Config
from src.services.llm_service import LLMService
from src.services.data_service import DataService
from src.ui.sidebar import render_sidebar
from src.ui.dashboard import render_dashboard
from src.ui.chat import render_chat

# 1. App Configuration
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    layout=Config.LAYOUT
)

# 2. State Initialization
if "emails" not in st.session_state:
    data_service = DataService()
    st.session_state.emails = data_service.load_inbox()

if "prompts" not in st.session_state:
    st.session_state.prompts = Config.DEFAULT_PROMPTS

# 3. Render UI Components
api_key = render_sidebar()

# Initialize Services
llm_service = LLMService(api_key=api_key, model_name=Config.DEFAULT_MODEL)
data_service = DataService()

# Clean Title (No Icon)
st.title(Config.PAGE_TITLE)

# 4. Main Navigation
tab1, tab2 = st.tabs(["Inbox Dashboard", "Email Agent"])

with tab1:
    render_dashboard(llm_service, data_service)

with tab2:
    render_chat(llm_service)