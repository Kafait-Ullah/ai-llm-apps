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

## Sample Review and Output

### Sample Input:
```plaintext
This leaf blower is pretty amazing. It has four settings: candle blower, gentle breeze, windy city, and tornado. It arrived in two days, just in time for my wife's anniversary present. I think my wife liked it so much she was speechless. So far I've been the only one using it, and I've been using it every other morning to clear the leaves on our lawn. It's slightly more expensive than the other leaf blowers out there, but I think it's worth it for the extra features.
```

### Output:
```json
{
   "gift": true,
   "delivery_days": 2,
   "price_value": ["It's slightly more expensive than the other leaf blowers out there", "I think it's worth it for the extra features"]
}
```

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
