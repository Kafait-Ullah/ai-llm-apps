import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import pycountry

st.header("🌍🔤 All Language Translator 🌐📝")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
review_text = st.text_area("Enter the text you need to translate:")

parser = StrOutputParser()

# Prompt template for translation
template = """
You are a professional translator. Please accurately translate the following text into {language}. Ensure the translation maintains the original meaning, tone, and context.

text: {text}
"""
prompt_template = ChatPromptTemplate.from_template(template)

# Generate a list of languages and their codes using pycountry
languages = {lang.name: lang.alpha_2 for lang in pycountry.languages if hasattr(lang, 'alpha_2')}
default_index = list(languages.keys()).index("English")
selected_language_name = st.selectbox('Select a language:', list(languages.keys()), index=default_index)
selected_language_code = languages[selected_language_name]


st.write(f'You selected: {selected_language_name} (Code: {selected_language_code})')

# Handle translation logic
if st.button("Translate Text", type="primary" ):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
        st.stop()
    elif not review_text:
        st.error("Please enter text to translate.")
        st.stop()
    else:
        # Initialize OpenAI LLM
        llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini", openai_api_key=api_key)

        # Create prompt messages
        messages = prompt_template.format_messages(text=review_text, language=selected_language_name)

        # Chain LLM and parser together
        chain = llm | parser
        output = chain.invoke(messages)

        # Display translated output
        st.write(output)
