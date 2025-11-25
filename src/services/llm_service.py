import google.generativeai as genai
import time
from typing import Optional

class LLMService:
    def __init__(self, api_key: str, model_name: str):
        self.api_key = api_key
        self.model_name = model_name
        self._configure()

    def _configure(self):
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)

    def generate(self, system_prompt: str, content: str) -> str:
        """
        Generates content using the LLM with error handling and rate limit protection.
        """
        if not self.api_key:
            return "Error: API Key is missing."

        try:
            full_prompt = f"SYSTEM INSTRUCTION: {system_prompt}\n\nCONTENT:\n{content}"
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"LLM Error: {str(e)}"
    
    def generate_safe(self, system_prompt: str, content: str) -> str:
        """
        Wrapper that adds a small delay to respect free tier limits.
        """
        response = self.generate(system_prompt, content)
        time.sleep(0.5) # Rate limit protection
        return response