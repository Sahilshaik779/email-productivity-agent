import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PAGE_TITLE = "Email Productivity Agent"
    LAYOUT = "wide"
    
    # Defaults
    DEFAULT_MODEL = "gemini-2.0-flash"
    API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Default Prompts
    DEFAULT_PROMPTS = {
        "categorize": (
            "Categorize this email into exactly one of these labels: "
            "Important, Newsletter, Spam, To-Do. Respond with ONLY the label name."
        ),
        "action_item": (
            "Extract tasks. Return strict JSON with keys: "
            "'tasks' (list of strings) and 'deadline' (string or null). "
            "If no tasks, return empty list."
        ),
        "reply": (
            "Draft a polite, professional reply. "
            "If it is a meeting request, ask for an agenda."
        )
    }