# AI News Digest – Automated AI News Aggregator & Email Delivery System

AI News Digest is a backend-driven automation pipeline that collects the latest AI-related content from multiple sources, processes and summarizes it using LLMs, ranks it based on user preferences, and delivers a curated email digest to users.

The system is designed with modular architecture, automation, and scalability in mind—making it suitable for real-world deployment and continuous background execution.

---

## Features

### 📰 Multi-Source Content Aggregation

* Scrapes AI-related content from:

  * YouTube (videos + transcripts)
  * OpenAI updates (if available)
  * Anthropic blogs (if available)
* Structured ingestion pipeline for extensibility

---

### 🧠 AI-Powered Digest Generation

* Uses LLMs (Gemini) to:

  * Summarize articles and videos
  * Generate concise, high-quality digests
* Focus on clarity, relevance, and actionable insights

---

### 🎯 Personalized Content Ranking

* Ranks digests based on:

  * User interests
  * Technical background
  * Expertise level
* Ensures most relevant content appears first

---

### 📧 Automated Email Delivery

* Generates HTML email digest
* Sends curated AI news directly to user inbox
* Runs on a scheduled pipeline (daily automation)

---

### ⚙️ End-to-End Pipeline Automation

* Fully automated workflow:

  1. Scrape → Process → Summarize → Rank → Email
* Designed to run via:

  * Cron jobs / Task Scheduler
  * Background workers

---

### 🗄️ Database Integration

* PostgreSQL for persistent storage
* Stores:

  * Articles
  * YouTube videos
  * Generated digests
* Structured schema for scalability

---

## Tech Stack

### Backend

* Python
* SQLAlchemy (ORM)
* Pydantic (data validation)

### AI / LLM

* Google Gemini (`google-genai`)

### Data Processing

* BeautifulSoup
* Feedparser
* Requests
* YouTube Transcript API

### Database

* PostgreSQL
* psycopg2

### Email & Automation

* SMTP / Email services
* Scheduled jobs (Cron / Task Scheduler)

---

## How It Works

### 1️⃣ Content Scraping

* Fetches latest AI-related content from multiple sources
* Stores raw data in database

---

### 2️⃣ Content Processing

* Extracts transcripts (YouTube)
* Cleans and structures text data

---

### 3️⃣ Digest Generation

* LLM generates:

  * Title
  * Summary
* Converts raw content into readable insights

---

### 4️⃣ Ranking Engine

* Uses user profile to rank digests
* Prioritizes relevance and usefulness

---

### 5️⃣ Email Generation & Delivery

* Converts ranked digests into HTML
* Sends email to user with curated content

---

## Run Locally

### Prerequisites

* Python 3.10+
* PostgreSQL
* Git

---

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-news-digest.git
cd ai-news-digest
```

---

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Setup Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/news_db
EMAIL_USER=your_email
EMAIL_PASSWORD=your_password
```

---

### Run the Pipeline

```bash
python main.py
```

---

## Project Structure

```bash
app/
├── agent/              # LLM agents (digest + ranking)
├── services/           # Email, processing, scraping
├── database/           # DB models and session
├── daily_runner.py     # Pipeline orchestrator
main.py                 # Entry point
```

---

## Future Improvements

* Add FastAPI for API layer
* Dockerize the application
* Add Redis queue for async processing
* Multi-user support with authentication
* Web dashboard for viewing digests
* Retry + fallback (Gemini → OpenAI)

---

## Key Highlights

* Fully automated AI content pipeline
* Clean modular architecture
* LLM-powered summarization + ranking
* Production-ready design foundation
