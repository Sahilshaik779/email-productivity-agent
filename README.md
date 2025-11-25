# Prompt-Driven Email Productivity Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini%202.0-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

An intelligent, prompt-driven email assistant built with **Python** and **Streamlit**. This agent leverages **Google Gemini (LLM)** to automatically categorize inboxes, extract structured action items, and generate context-aware reply drafts.

The system features a **modular prompt architecture**, allowing users to configure the "Agent Brain" (prompts) directly from the UI without changing code.

---

## Features

* **Smart Inbox Ingestion**
    * Loads mock email data from JSON.
    * Visual dashboard for reviewing email content, senders, and metadata.
* **Automated Categorization**
    * Classifies emails into configurable tags: *Important, Newsletter, Spam, To-Do*.
    * Powered by the `gemini-2.0-flash` model for high-speed processing.
* **Action Item Extraction**
    * Parses email bodies to identify specific tasks and deadlines.
    * Outputs strictly formatted JSON data for downstream integration.
* **"Prompt Brain" Architecture**
    * **User-Configurable:** Edit categorization rules, extraction logic, and reply personalities in real-time via the Sidebar.
    * **State Persistence:** Prompt settings are saved during the active session.
* **Interactive Agent**
    * Chat with specific emails (e.g., "Summarize this thread").
    * **Auto-Drafter:** Generates safe, reviewable email drafts based on context.

---

## Tech Stack & Architecture

This project follows a **Service-Oriented Architecture (SOA)** with a clean separation of concerns:

* **Frontend:** Streamlit (UI components in `src/ui/`)
* **Backend Logic:** Python Services (`src/services/`)
    * `llm_service.py`: Handles API communication and rate limiting.
    * `data_service.py`: Manages JSON I/O and data parsing.
* **AI Engine:** Google Gemini API (`gemini-2.0-flash`).
* **Data Store:** JSON (Mock Inbox) & In-Memory Session State.

---

## Installation & Setup

### Prerequisites
* Python 3.8 or higher.
* A Google Cloud API Key (for Gemini).

### 1. Clone the Repository
```bash
git clone https://github.com/Sahilshaik779/email-productivity-agent.git
cd email-productivity-agent
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory. Add your Google API Key:
```text
GOOGLE_API_KEY=your_actual_api_key_here
```
*(Note: The `.env` file is git-ignored for security).*

---

## Usage Guide

### Running the Application
Execute the main entry point via Streamlit:
```bash
streamlit run main.py
```

### Phase 1: Inbox Dashboard
1.  Navigate to the **"Inbox Dashboard"** tab.
2.  Click the **"Process Inbox"** button.
3.  The agent will iterate through the `mock_inbox.json` file:
    * **Category Column:** Displays the LLM-assigned tag (e.g., Important, Spam).
    * **Actions Column:** Displays the extracted JSON (Tasks/Deadlines).

### Phase 2: Agent Brain Configuration
1.  Open the **Sidebar**.
2.  Locate the **"Agent Logic"** section.
3.  Edit the text areas to change behavior (e.g., change the *Reply Personality* from "Professional" to "Brief").
4.  Click **"Save Configuration"**.
5.  Rerun the inbox processing to see the changes take effect immediately.

### Phase 3: Agent Workspace
1.  Switch to the **"Email Agent"** tab.
2.  **Select an Email** from the dropdown menu to set the context.
3.  **Draft Assistant:** Click "Auto-Draft Reply" to generate a response based on your configuration.
4.  **Context Chat:** Type a custom query (e.g., "Who is the sender?") to chat with the email content.

---

## Project Structure

```text
├── src/
│   ├── services/          # Business logic (LLM & Data)
│   ├── ui/                # Streamlit UI components
│   └── config.py          # Centralized configuration
├── mock_inbox.json        # Sample email data (Project Asset)
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
├── .env                   # API Secrets (Excluded from Git)
└── README.md              # Project documentation
```

## License
This project is developed for the **AI Agent Assignment**.