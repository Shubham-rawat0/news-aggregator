import os
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class EmailIntroduction(BaseModel):
    greeting: str = Field(description="Personalized greeting with user's name and date")
    introduction: str = Field(description="2-3 sentence overview of top ranked articles")

class RankedArticleDetail(BaseModel):
    digest_id: str
    rank: int
    relevance_score: float
    title: str
    summary: str
    url: str
    article_type: str
    reasoning: Optional[str] = None

class EmailDigestResponse(BaseModel):
    introduction: EmailIntroduction
    articles: List[RankedArticleDetail]
    total_ranked: int
    top_n: int

    def to_markdown(self) -> str:
        md = f"{self.introduction.greeting}\n\n"
        md += f"{self.introduction.introduction}\n\n---\n\n"

        for article in self.articles:
            md += f"## {article.title}\n\n"
            md += f"{article.summary}\n\n"
            md += f"[Read more →]({article.url})\n\n---\n\n"

        return md

class EmailAgent:
    def __init__(self, user_profile: dict):
        self.user_profile = user_profile

    def _normalize_articles(self, ranked_articles: List) -> List[RankedArticleDetail]:
        normalized = []
        for a in ranked_articles:
            if isinstance(a, RankedArticleDetail):
                normalized.append(a)
            else:
                normalized.append(RankedArticleDetail(**a))
        return normalized

    def generate_introduction(self, ranked_articles: List[RankedArticleDetail]) -> EmailIntroduction:
        current_date = datetime.now().strftime('%B %d, %Y')

        greeting = f"Hey {self.user_profile['name']}, here is your daily digest of AI news for {current_date}."

        if not ranked_articles:
            return EmailIntroduction(
                greeting=greeting,
                introduction="No relevant AI updates were found today."
            )

        top_articles = ranked_articles[:10]

        types = [a.article_type.lower() for a in top_articles]
        unique_types = set(types)

        intro_parts = []

        if "research" in unique_types:
            intro_parts.append("latest research developments")
        if "product" in unique_types:
            intro_parts.append("new AI product launches")
        if "news" in unique_types:
            intro_parts.append("important industry updates")

        if not intro_parts:
            intro_parts.append("key AI updates")

        intro_text = ", ".join(intro_parts)

        introduction = (
            f"Today’s top {len(top_articles)} articles cover {intro_text}. "
            f"These were selected based on your interests and relevance scores."
        )

        return EmailIntroduction(
            greeting=greeting,
            introduction=introduction
        )

    def create_email_digest_response(
        self,
        ranked_articles: List,
        total_ranked: int,
        limit: int = 10
    ) -> EmailDigestResponse:

        ranked_articles = self._normalize_articles(ranked_articles)

        top_articles = ranked_articles[:limit]
        introduction = self.generate_introduction(top_articles)

        return EmailDigestResponse(
            introduction=introduction,
            articles=top_articles,
            total_ranked=total_ranked,
            top_n=limit
        )