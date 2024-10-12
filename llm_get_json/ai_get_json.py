# Differences between the First and Second Code:
# 1. First uses a basic parser; second uses StructuredOutputParser.
# 2. First lacks schemas; second defines schemas for `gift`, `delivery_days`, `price_value`.
# 3. First has no format instructions; second includes structured format instructions.

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Set the title of the app
st.header("Customer Review Analyzer")

# Input for OpenAI API Key (to access OpenAI's API)
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Input for customer review
review_text = st.text_area("Enter the customer review below:")

# Initialize the output parser
parser = StrOutputParser()

# Define the prompt template to extract specific information from the review
review_template = """
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? 
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product 
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,
and output them as a comma-separated Python list.

Format the output as JSON with the following keys:
gift
delivery_days
price_value

text: {text}
"""

# Create a prompt from the template
prompt_template = ChatPromptTemplate.from_template(review_template)

# Button to trigger analysis
if st.button("Analyze Review"):
    # Check if API key is provided
    if not api_key:
        st.error("Please enter your OpenAI API key.")
        st.stop()

    # Check if review text is provided
    elif not review_text:
        st.error("Please enter a customer review.")
        st.stop()
    else:
        # Initialize the language model with specified parameters
        llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini", openai_api_key=api_key)
        
        # Format the messages for the model
        messages = prompt_template.format_messages(text=review_text)
        
        # Invoke the model and get the output
        chain = llm | parser
        output = chain.invoke(messages)
        
        # Display the output in the app
        st.write(output)











# import streamlit as st
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain.output_parsers import ResponseSchema
# from langchain.output_parsers import StructuredOutputParser

# # Set the title of the app
# st.header("Customer Review Analyzer")

# # Input for OpenAI API Key (to access OpenAI's API)
# api_key = st.text_input("Enter your OpenAI API Key", type="password")

# # Input for customer review
# review_text = st.text_area("Enter the customer review below:")

# # Initialize the output parser
# parser = StrOutputParser()

# # Define response schemas for structured output
# gift_schema = ResponseSchema(name="gift",
#                              description="Was the item purchased as a gift for someone else? "
#                              "Answer True if yes, False if not or unknown.")
# delivery_days_schema = ResponseSchema(name="delivery_days",
#                                       description="How many days did it take for the product "
#                                       "to arrive? If this information is not found, output -1.")
# price_value_schema = ResponseSchema(name="price_value",
#                                     description="Extract any sentences about the value or "
#                                     "price, and output them as a comma-separated Python list.")

# # Combine response schemas into a list
# response_schemas = [gift_schema, 
#                     delivery_days_schema,
#                     price_value_schema]

# # Define the prompt template for structured output
# review_template_2 = """\
# For the following text, extract the following information:

# gift: Was the item purchased as a gift for someone else? 
# Answer True if yes, False if not or unknown.

# delivery_days: How many days did it take for the product to arrive? If this information is not found, output -1.

# price_value: Extract any sentences about the value or price, and output them as a comma-separated Python list.

# text: {text}

# {format_instructions}
# """

# # Button to trigger analysis
# if st.button("Analyze Review"):
#     # Check if API key is provided
#     if not api_key:
#         st.error("Please enter your OpenAI API key.")
#         st.stop()

#     # Check if review text is provided
#     elif not review_text:
#         st.error("Please enter a customer review.")
#         st.stop()
#     else:
#         # Initialize the language model with specified parameters
#         llm = ChatOpenAI(temperature=0.0, model="gpt-4o-mini", openai_api_key=api_key)

#         # Create a prompt from the template
#         prompt = ChatPromptTemplate.from_template(template=review_template_2)

#         # Create a structured output parser from response schemas
#         output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        
#         # Get formatting instructions for the parser
#         format_instructions = output_parser.get_format_instructions()
                    
#         # Format the messages for the model
#         messages = prompt.format_messages(text=review_text, 
#                                            format_instructions=format_instructions)
        
#         # Invoke the model and get the structured output
#         chain = llm | output_parser
#         output = chain.invoke(messages)

#         # Display the output in the app
#         st.write(output)
