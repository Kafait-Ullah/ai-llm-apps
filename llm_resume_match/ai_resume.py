import streamlit as st
import PyPDF2
from groq import Groq
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Streamlit UI setup
st.set_page_config(page_title="ResumeMatch AI", page_icon="📄", layout="wide")
st.title("ResumeMatch AI: Smart Candidate Screener")
st.markdown("*Powered by AI to streamline your hiring process*")

api_key = st.text_input("Enter your API Key (OpenAI or Groq):", type="password")

# Add a single text input for job requirements
st.subheader("Job Requirements")
job_requirements = st.text_area("Enter the job requirements (skills, experience, qualifications, etc.):")

# File uploader for PDF resumes
uploaded_files = st.file_uploader("Upload Resumes (PDFs)", type=["pdf"], accept_multiple_files=True)

# Function to extract text from PDFs using PyPDF2
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

# Function to determine whether to use OpenAI or Groq and process the resumes
def process_resumes(api_key, resumes, job_requirements):
    eligible_candidates = []
    ineligible_candidates = []

    if api_key.startswith("sk-"):  # OpenAI API Key
        st.write("Using OpenAI API for processing...")
        model = ChatOpenAI(model="gpt-4", temperature=0.0, openai_api_key=api_key)

        for uploaded_file in resumes:
            resume_text = extract_text_from_pdf(uploaded_file)

            # Generate the prompt for parsing the resume
            prompt = f"Extract the name, contact details, work experience (in months/years), and skills from the following resume:\n\n{resume_text}"

            try:
                ai_message = model.invoke([HumanMessage(content=prompt)])
                resume_output = ai_message.content

                # Generate a prompt to match with job requirements
                match_prompt = f"Based on the following job requirements:\n{job_requirements}\n\n" \
                               f"And the following resume details:\n{resume_output}\n\n" \
                               "Is this candidate eligible for the job? Consider if the candidate meets or exceeds the experience requirements. " \
                               "Give a yes or no answer, and explain why."

                match_message = model.invoke([HumanMessage(content=match_prompt)])
                match_output = match_message.content

                candidate_info = extract_candidate_info(resume_output, uploaded_file.name)
                candidate_info['eligibility'] = match_output

                if "yes" in match_output.lower():
                    eligible_candidates.append(candidate_info)
                else:
                    ineligible_candidates.append(candidate_info)

            except Exception as e:
                st.error(f"Error processing resume {uploaded_file.name}: {e}")

    else:  # Groq API Key
        st.write("Using Groq API for processing...")
        client = Groq(api_key=api_key)

        for uploaded_file in resumes:
            resume_text = extract_text_from_pdf(uploaded_file)

            try:
                # Create Groq completion call for resume parsing
                completion = client.chat.completions.create(
                    model="llama3-groq-70b-8192-tool-use-preview",
                    messages=[{
                        "role": "user",
                        "content": f"Extract name, contact details, work experience (in months/years), and skills from the following resume:\n\n{resume_text}"
                    }],
                    temperature=0.5,
                    max_tokens=1024,
                    top_p=0.65,
                    stream=True,
                    stop=None,
                )

                resume_output = ""
                for chunk in completion:
                    resume_output += chunk.choices[0].delta.content or ""

                # Create Groq completion call for candidate matching
                match_prompt = f"Based on the following job requirements:\n{job_requirements}\n\n" \
                               f"And the following resume details:\n{resume_output}\n\n" \
                               "Is this candidate eligible for the job? Consider if the candidate meets or exceeds the experience requirements. " \
                               "Give a yes or no answer, and explain why."

                completion = client.chat.completions.create(
                    model="llama3-groq-70b-8192-tool-use-preview",
                    messages=[{
                        "role": "user",
                        "content": match_prompt
                    }],
                    temperature=0.5,
                    max_tokens=1024,
                    top_p=0.65,
                    stream=True,
                    stop=None,
                )

                match_output = ""
                for chunk in completion:
                    match_output += chunk.choices[0].delta.content or ""

                candidate_info = extract_candidate_info(resume_output, uploaded_file.name)
                candidate_info['eligibility'] = match_output

                if "yes" in match_output.lower():
                    eligible_candidates.append(candidate_info)
                else:
                    ineligible_candidates.append(candidate_info)

            except Exception as e:
                st.error(f"Error processing resume {uploaded_file.name}: {e}")

    return eligible_candidates, ineligible_candidates

# Helper function to extract candidate details from parsed resume output
def extract_candidate_info(resume_output, filename):
    name = "Name not found"
    contact_details = "Contact details not found"
    
    # Extract name from the resume output
    if "Name:" in resume_output:
        name = resume_output.split("Name:")[1].split("\n")[0].strip()
    
    # Extract contact details like email, phone, LinkedIn, etc.
    if "Contact Details:" in resume_output:
        contact_details = resume_output.split("Contact Details:")[1].strip()
    
    return {
        "name": name,
        "contact": contact_details,
        "resume_output": resume_output,
        "filename": filename
    }

# Match candidates and show results
if st.button("Screen Candidates"):
    if api_key and uploaded_files and job_requirements:
        with st.spinner('Processing resumes... This may take a moment.'):
            eligible_candidates, ineligible_candidates = process_resumes(api_key, uploaded_files, job_requirements)

        # Display the results in a professional and well-organized format
        if eligible_candidates:
            st.markdown("## ✅ Eligible Candidates:")
            for candidate in eligible_candidates:
                st.markdown(f"### Candidate Name: **{candidate['name']}**")
                st.markdown(f"**File:** {candidate['filename']}")
                st.markdown(f"**Contact Details:** {candidate['contact'] if 'Contact details not found' not in candidate['contact'] else 'No contact details found'}")
                st.markdown("**Eligibility Reason:**")
                st.markdown(candidate['eligibility'])
                with st.expander("View Resume Details"):
                    st.code(candidate['resume_output'], language="text")
                st.markdown("---")  # Divider for each candidate

        if ineligible_candidates:
            st.markdown("## ❌ Ineligible Candidates:")
            for candidate in ineligible_candidates:
                st.markdown(f"### Candidate Name: **{candidate['name']}**")
                st.markdown(f"**File:** {candidate['filename']}")
                st.markdown(f"**Contact Details:** {candidate['contact'] if 'Contact details not found' not in candidate['contact'] else 'No contact details found'}")
                st.markdown("**Ineligibility Reason:**")
                st.markdown(candidate['eligibility'])
                with st.expander("View Resume Details"):
                    st.code(candidate['resume_output'], language="text")
                st.markdown("---")  # Divider for each candidate

    else:
        st.warning("Please enter your API key, upload at least one resume, and provide job requirements.")

# Add a footer
st.markdown("---")
st.markdown("ResumeMatch AI © 2024 - Streamlining recruitment with artificial intelligence")

