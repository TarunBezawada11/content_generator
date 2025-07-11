import mysql.connector
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

def get_tone_template(persona, tone):
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "Password@123"),
            database=os.getenv("DB_NAME", "template_for_tones")
        )
    except mysql.connector.Error as err:
        print("Error connecting to the database:", err)
        return None

    cursor = conn.cursor()
    query = "SELECT template FROM tone_templates WHERE persona = %s AND mood = %s"

    cursor.execute(query, (persona.strip().lower(), tone.strip().lower()))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

def select_length(word_limit_choice):
    if word_limit_choice == "200-250":
        return 200, "Length: 200-250 words"
    elif word_limit_choice == "300-350":
        return 250, "Length: 300-350 words"
    elif word_limit_choice == "400-450":
        return 350, "Length: 400-450 words"
    else:
        return 150, "Length: approx. 150 words"

def build_prompt(template, topic, length_instruction):
    return f"{template}\nTopic: {topic}\n({length_instruction})"

def generate_post(final_prompt, max_tokens):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="meta-llama/llama-4-scout-17b-16e-instruct"
    )
    try:
        response = llm.invoke(final_prompt)
        return response.content.strip()
    except Exception as e:
        return f"Error during generation: {str(e)}"
