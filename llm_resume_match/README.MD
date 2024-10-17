# 🚀📄 ResumeMatch AI: Smart Candidate Screener 💼🤖

ResumeMatch AI is a powerful Streamlit-based application that revolutionizes the hiring process by leveraging AI to screen resumes against job requirements. This tool uses OpenAI's GPT-4 or Groq's LLM to provide intelligent candidate matching and assessment, streamlining the recruitment process for HR professionals and hiring managers.

## 🌟 Features

- **AI-Powered Resume Analysis**: Harness the power of advanced language models to parse and comprehend resume content.
- **Automatic Eligibility Assessment**: Seamlessly match candidate skills and experience against specified job requirements.
- **Multi-API Support**: Flexibility to use either OpenAI (GPT-4) or Groq APIs for analysis.
- **Bulk PDF Processing**: Efficiently analyze multiple resumes simultaneously.
- **User-Friendly Interface**: Clean and intuitive Streamlit-based UI for ease of use.
- **Detailed Output**: Comprehensive insights on each candidate's eligibility, including specific reasons for matching or non-matching.
- **Customizable**: Easily adaptable to specific hiring needs and criteria.

## 🛠️ Prerequisites

- **Python 3.8+**: Ensure you have a compatible Python version installed.
- **OpenAI API Key or Groq API Key**: Valid API key from either service.
- **Required Libraries**: 
  - Streamlit
  - PyPDF2
  - langchain_openai
  - groq

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kafait-Ullah/ai-llm-apps.git
   cd resumematch-ai
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
   streamlit run resumematch_ai.py
   ```

## 🚀 Usage

1. **Launch the App**: Open the provided URL after running the Streamlit command.
2. **Enter API Key**: Input your OpenAI or Groq API key in the designated field.
3. **Specify Job Requirements**: Detail the job requirements in the text area provided.
4. **Upload Resumes**: Use the file uploader to select PDF resumes for screening.
5. **Initiate Screening**: Click the "Screen Candidates" button to start the AI-driven analysis.
6. **Review Results**: Examine the output, which categorizes candidates into eligible and ineligible groups, providing detailed reasoning for each.

## 💡 How It Works

1. **Resume Parsing**: The application extracts text content from uploaded PDF resumes using PyPDF2.
2. **AI Analysis**: Utilizes GPT-4 or Groq to analyze the extracted resume content against the provided job requirements.
3. **Matching Algorithm**: Determines candidate eligibility based on the AI-generated insights, considering factors like skills, experience, and qualifications.
4. **Result Presentation**: Displays a comprehensive breakdown of each candidate's suitability, including specific reasons for eligibility or ineligibility.

## 🔒 Privacy and Security

- **API Key Handling**: API keys are processed securely and are not stored or logged.
- **Data Processing**: Resume data is processed in-memory and is not persisted or shared.
- **Local Operation**: All processing occurs locally on your machine, ensuring data privacy.

## 🔧 Customization

The application can be easily customized to fit specific recruitment needs:

- Modify the prompt templates in the code to focus on particular aspects of candidate assessment.
- Adjust the eligibility criteria by updating the logic in the `process_resumes` function.
- Extend the UI to include additional inputs or outputs as needed for your hiring process.

## 🤝 Contributing

Contributions to improve ResumeMatch AI are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Kafait-Ullah/ai-llm-apps/LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI and Groq for providing powerful language models
- The Streamlit team for their fantastic framework
- All contributors and users of this tool

---

Created with ❤️ by [Kafait Ullah](https://github.com/Kafait-Ullah)