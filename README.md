# Prompt-Driven Email Productivity Agent

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
git clone [https://github.com/Sahilshaik779/email-productivity-agent.git](https://github.com/Sahilshaik779/email-productivity-agent.git)
cd email-productivity-agent