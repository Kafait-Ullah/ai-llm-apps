# 📝 Customer Review Analyzer

This Streamlit app enables users to analyze customer reviews using the power of GPT-4o. It extracts specific information from reviews, such as whether the product was a gift, delivery times, and comments on pricing/value.

## Features
- Extracts key information such as:
  - Whether the product was purchased as a gift
  - Number of days taken for delivery
  - Sentences related to price/value
- Outputs the extracted information in a structured JSON format
- User-friendly interface powered by Streamlit

## How to Get Started
1. **Clone the GitHub repository**:
   ```bash
   git clone https://github.com/Kafait-Ullah/ai-llm-apps.git
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your OpenAI API Key**:
   - Sign up for an OpenAI account and obtain your API key.

4. **Run the Streamlit App**:
   ```bash
   streamlit run review_analyzer.py
   ```

## How It Works
- When you run the app, it prompts you to input your OpenAI API key.
- Enter the review text you want to analyze.
- The app uses a language model (GPT-4o) to process the review and extract specific information such as whether the product was a gift, delivery time, and price-related sentences.
- The app will display the structured output as JSON.

## Output Format
The extracted information is returned in the following structure:
```json
{
   "gift": true,
   "delivery_days": 3,
   "price_value": ["The price was reasonable", "It’s a bit expensive for what you get"]
}
```

## Contribution
Feel free to submit pull requests to improve the app or suggest additional features!
