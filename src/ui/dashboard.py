import streamlit as st
from src.services.llm_service import LLMService
from src.services.data_service import DataService

def render_dashboard(llm_service: LLMService, data_service: DataService):
    st.header("Inbox Dashboard")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.markdown("### Actions")
        if st.button("Process Inbox", type="primary", use_container_width=True):
            _process_emails(llm_service, data_service)
            
    with col2:
        emails = st.session_state.get("emails", [])
        if emails:
            df = data_service.to_dataframe(emails)
            # Smart Column Selection
            display_cols = ['sender', 'subject']
            if 'category' in df.columns: display_cols.append('category')
            if 'actions' in df.columns: display_cols.append('actions')
            
            st.dataframe(
                df[display_cols], 
                use_container_width=True, 
                hide_index=True,
                height=500
            )
        else:
            st.info("Inbox is empty. Check mock_inbox.json.")

def _process_emails(llm: LLMService, data_svc: DataService):
    """Helper function to run the batch processing pipeline."""
    emails = st.session_state.emails
    prompts = st.session_state.prompts
    
    progress = st.progress(0)
    status = st.empty()
    
    for i, email in enumerate(emails):
        status.caption(f"Processing: {email['subject']}...")
        
        # Pipeline Step 1: Categorize
        cat = llm.generate_safe(prompts["categorize"], email['body'])
        st.session_state.emails[i]['category'] = cat
        
        # Pipeline Step 2: Extract Actions
        raw_actions = llm.generate_safe(prompts["action_item"], email['body'])
        st.session_state.emails[i]['actions'] = data_svc.clean_json_output(raw_actions)
        
        progress.progress((i + 1) / len(emails))
        
    status.success("Processing Complete")
    st.rerun()