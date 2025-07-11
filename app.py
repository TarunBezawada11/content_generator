import streamlit as st
from dotenv import load_dotenv
from LLM_post_generator import get_tone_template, select_length, build_prompt, generate_post

load_dotenv()

def main():
    st.set_page_config(page_title="AI Post Generator", layout="centered")

    st.title("🧠 AI Post Generator")
    st.caption("create your own tone")

    # Persona, Tone, Word Count, Topic
    persona = st.selectbox("Select Persona:", [
        "elon", "bill gates", "zuck", "sam altman", "donald trump",
        "general", "fluent", "academic"
    ])

    tone = st.selectbox("Select Tone:", [
        "witty", "motivational", "analytical", "inspirational", "direct"
    ])

    word_limit_choice = st.selectbox("Choose word count:", [
        "200-250", "300-350", "400-450"
    ])

    topic = st.text_input("Enter the topic for the post:",
                          value="Write a post about the future of renewable energy.")

    if st.button("Generate Post"):
        with st.spinner("Generating post with LLaMA-4..."):
            template = get_tone_template(persona, tone)
            if not template:
                st.error(f"No template found for persona '{persona}' and tone '{tone}'.")
                return

            max_tokens, length_instruction = select_length(word_limit_choice)
            final_prompt = build_prompt(template, topic, length_instruction)

            st.markdown("### 🔧 Prompt Sent to LLM")
            st.code(final_prompt, language="text")

            generated_post = generate_post(final_prompt, max_tokens)

            st.markdown("### 📝 Generated Post")
            st.success(generated_post)

if __name__ == "__main__":
    main()
