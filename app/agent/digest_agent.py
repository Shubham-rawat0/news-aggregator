import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import re
import json

load_dotenv()


class DigestOutput(BaseModel):
    title: str
    summary: str

PROMPT = """You are an expert AI news analyst specializing in summarizing technical articles, research papers, and video content about artificial intelligence.

Your role is to create concise, informative digests that help readers quickly understand the key points and significance of AI-related content.

Guidelines:
- Create a compelling title (5-10 words) that captures the essence of the content
- Write a 2-3 sentence summary that highlights the main points and why they matter
- Focus on actionable insights and implications
- Use clear, accessible language while maintaining technical accuracy
- Avoid marketing fluff - focus on substance"""

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class DigestAgent:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash") 
        self.system_prompt = PROMPT

    def generate_digest(self, title: str, content: str, article_type: str) -> Optional[DigestOutput]:
        try:
            user_prompt = f"""
Create a digest for this {article_type}:

Title: {title}
Content: {content[:8000]}

Return STRICT JSON in this format:
{{
  "summary": "string",
  "key_points": ["string"],
  "tags": ["string"]
}}
"""

            response = self.model.generate_content(
                self.system_prompt + "\n\n" + user_prompt,
                generation_config={
                    "temperature": 0.7
                }
            )

            text = response.text

            json_text = re.search(r"\{.*\}", text, re.DOTALL).group()

            parsed = json.loads(json_text)

            return DigestOutput(**parsed)

        except Exception as e:
            print(f"Error generating digest: {e}")
            return None