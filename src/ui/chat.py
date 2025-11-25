import streamlit as st
from src.services.llm_service import LLMService

def render_chat(llm_service: LLMService):
    st.header("Agent Workspace")
    
    emails = st.session_state.get("emails", [])
    if not emails:
        st.warning("No emails to process.")
        return

    # Sidebar-style selection within the tab
    email_map = {f"{e['id']} | {e['subject']}": e for e in emails}
    selected_key = st.selectbox("Select an email context:", list(email_map.keys()))
    
    if selected_key:
        email = email_map[selected_key]
        
        # Context Viewer
        with st.expander("View Email Context", expanded=True):
            st.markdown(f"**From:** `{email['sender']}`  **Subject:** `{email['subject']}`")
            st.text(email['body'])
            
            if 'actions' in email:
                st.caption("Extracted Metadata:")
                st.code(email['actions'], language="json")

        st.divider()

        # Two-Column Layout for Tools
        c1, c2 = st.columns(2)
        
        with c1:
            st.subheader("Draft Assistant")
            if st.button("Auto-Draft Reply"):
                with st.spinner("Writing..."):
                    prompt = st.session_state.prompts["reply"]
                    draft = llm_service.generate(prompt, email['body'])
                    st.text_area("Generated Draft", value=draft, height=300)
                    st.success("Draft ready for review.")

        with c2:
            st.subheader("Context Chat")
            query = st.text_input("Ask about this email:")
            if query and st.button("Ask Agent"):
                with st.spinner("Thinking..."):
                    resp = llm_service.generate(f"Answer this: {query}", email['body'])
                    st.markdown("### Agent Response")
                    st.write(resp)