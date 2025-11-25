import json
import pandas as pd
from typing import List, Dict, Any

class DataService:
    def __init__(self, filepath: str = "mock_inbox.json"):
        self.filepath = filepath

    def load_inbox(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filepath, "r") as f:
                content = f.read()
                return json.loads(content) if content else []
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def clean_json_output(self, llm_output: str) -> str:
        """Removes markdown formatting from LLM JSON responses."""
        return llm_output.replace("```json", "").replace("```", "").strip()

    def to_dataframe(self, emails: List[Dict]) -> pd.DataFrame:
        if not emails:
            return pd.DataFrame()
        return pd.DataFrame(emails)