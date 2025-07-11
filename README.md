# AI Content Generator with Groq LLaMA 4 and MySQL Tone Templates

This project is an AI-powered content generator built using the Groq LLaMA 4 API via LangChain. It dynamically generates posts based on selected personas and tones stored in a MySQL database. The app is built with Python and Streamlit.

---

## Features

- Supports multiple personas (e.g., Elon Musk, Sam Altman, Bill Gates) and tones (witty, motivational, analytical, etc.)
- Retrieves persona and tone templates from a MySQL database for dynamic prompt generation
- Uses Groq's LLaMA 4 Scout model for generating AI content
- Easy integration with environment variables for secure API key management
- Streamlit web app interface for interactive content generation

---

## Prerequisites

- Python 3.8+
- MySQL Server with `tone_templates` table setup (see Database Setup below)
- Groq API Key (sign up at [Groq](https://groq.com))
- `pip` packages:
  - `mysql-connector-python`
  - `streamlit`
  - `python-dotenv`
  - `langchain`
  - `langchain_groq`

---

## Database Setup

Create a MySQL database and the `tone_templates` table with this structure:

```sql
CREATE TABLE tone_templates (
  id INT PRIMARY KEY,
  persona VARCHAR(255),
  tone VARCHAR(255),
  template TEXT
);

-- Insert your persona-tone templates here
INSERT INTO tone_templates (id, persona, tone, template) VALUES
(1, 'elon', 'witty', 'Write in Elon Musk’s tone with a witty, clever, and humor-filled style.'),
(16, 'sam altman', 'witty', 'Write in Sam Altman’s tone with a witty, playful, and insightful style.'),
-- Add other rows as needed
;
