# 🌍🔤 All Language Translator 🌐📝

This **All Language Translator** is a Streamlit-based application that allows users to translate text into various languages using OpenAI's GPT-4 model. The app provides a seamless way to choose from a wide range of languages and delivers translations while preserving the original tone and meaning of the text.

## Features

- **API Key Input**: Users can securely input their OpenAI API key.
- **Text Translation**: Translate any input text into a selected language.
- **Multi-Language Support**: Supports a broad range of languages via pycountry.
- **Interactive UI**: A simple and clean user interface for easy input and output.

## How It Works

1. **API Key**: The user inputs their OpenAI API key.
2. **Text Input**: Enter the text you wish to translate.
3. **Language Selection**: Choose the target language from a dropdown menu.
4. **Translation Process**: The app leverages GPT-4 to generate accurate translations.
5. **Translated Output**: The translated text is displayed within the app.

## Prerequisites

- **Python 3.8+**: Ensure that you have Python installed.
- **OpenAI API Key**: A valid API key from OpenAI.

## Installation

1. Clone the repository:
   ```bash
   git clone  https://github.com/Kafait-Ullah/ai-llm-apps.git
   cd all-language-translator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter OpenAI API Key**: Provide your OpenAI API key in the input field.
2. **Input Text**: Type or paste the text to be translated.
3. **Select Language**: Pick the language you want the text translated into from the dropdown.
4. **Translate**: Click the **Translate Text** button to receive the translated output.

## Code Overview

### `ChatPromptTemplate`
A prompt template is used to structure the translation request in a way that the OpenAI model understands. It preserves the original context, meaning, and tone in the translation.

### `pycountry`
This library is used to generate a list of languages and their ISO 639-1 codes for language selection.

### OpenAI API Integration
The app integrates with the GPT-4 model by OpenAI to perform translations, and the user must provide their API key for this functionality.

### Error Handling
The app ensures that the user is alerted if required inputs (like API key or text) are missing and gracefully handles any potential API errors.


## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and create a pull request.

