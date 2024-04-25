# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     responses = []
#     for pdf in pdf_content:
#         response = model.generate_content([input_text, pdf, prompt])
#         responses.append(response.text)
#     return responses

# def input_pdf_setup(uploaded_files):
#     pdf_parts = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Convert the PDF to image
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_part = {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#             pdf_parts.append(pdf_part)
#     return pdf_parts

# # Streamlit App
# st.set_page_config(page_title="Job suggestion by the resume analysis")
# st.header("Job Eligible prediction by resume analysis")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
# Please share your professional evaluation on whether the candidates' profiles align with the role. 
# Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resumes against the provided job description. 
# Give me the percentage of match if the resumes match the job description. 
# First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
# """

# if submit1:
#     if uploaded_files:
#         pdf_content = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The Responses are:")
#         for i, response in enumerate(responses):
#             st.write(f"Response for Resume {i + 1}:")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# elif submit3:
#     if uploaded_files:
#         pdf_content = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("The Responses are:")
#         for i, response in enumerate(responses):
#             st.write(f"Response for Resume {i + 1}:")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")












#code 2 gives the percentage of the each of the candidate with alignment






from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt, candidate_names):
    model = genai.GenerativeModel('gemini-pro-vision')
    responses = []
    for name, pdf in zip(candidate_names, pdf_content):
        response = model.generate_content([input_text, pdf, prompt])
        responses.append((name, response.text))
    return responses

def input_pdf_setup(uploaded_files):
    pdf_parts = []
    candidate_names = []
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            # Extract candidate name from the file name
            name = os.path.splitext(uploaded_file.name)[0]
            candidate_names.append(name)

            # Convert the PDF to image
            images = pdf2image.convert_from_bytes(uploaded_file.read())
            first_page = images[0]

            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_part = {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
            pdf_parts.append(pdf_part)
    return pdf_parts, candidate_names

# Streamlit App
st.set_page_config(page_title="Job suggestion by the resume analysis")
st.header("Job Eligible prediction by resume analysis")
input_text = st.text_area("Job Description: ", key="input")
uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
Please share your professional evaluation on whether the candidates' profiles align with the role. 
Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resumes against the provided job description. 
Give me the percentage of match if the resumes match the job description. 
First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
"""

if submit1:
    if uploaded_files:
        pdf_content, candidate_names = input_pdf_setup(uploaded_files)
        responses = get_gemini_response(input_text, pdf_content, input_prompt1, candidate_names)
        st.subheader("The Responses are:")
        for name, response in responses:
            st.write(f"Candidate: {name}")
            st.write(response)
    else:
        st.write("Please upload at least one resume")

elif submit3:
    if uploaded_files:
        pdf_content, candidate_names = input_pdf_setup(uploaded_files)
        responses = get_gemini_response(input_text, pdf_content, input_prompt3, candidate_names)
        st.subheader("The Responses are:")
        for name, response in responses:
            st.write(f"Candidate: {name}")
            st.write(response)
    else:
        st.write("Please upload at least one resume")



















# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_text, pdf_content, prompt, candidate_names):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     responses = []
#     for name, pdf in zip(candidate_names, pdf_content):
#         response = model.generate_content([input_text, pdf, prompt])
#         responses.append((name, response.text))
#     return responses

# def input_pdf_setup(uploaded_files):
#     pdf_parts = []
#     candidate_names = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Extract candidate name from the file name
#             name = os.path.splitext(uploaded_file.name)[0]
#             candidate_names.append(name)

#             # Convert the PDF to image
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_part = {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#             pdf_parts.append(pdf_part)
#     return pdf_parts, candidate_names

# # def rank_resumes(responses):
# #     ranked_responses = []
# #     for name, response in responses:
# #         try:
# #             # Extract percentage match from the response text
# #             match_line = response.split("\n")[0]
# #             if "Percentage match" in match_line:
# #                 percentage_match = match_line.split(":")[1].strip().strip("%")
# #                 percentage_match = float(percentage_match)
# #             else:
# #                 raise ValueError("Percentage match not found")
            
# #             ranked_responses.append((name, response, percentage_match))
# #         except IndexError:
# #             st.error(f"Error processing response for {name}: Index out of range")
# #         except ValueError:
# #             st.error(f"Error processing response for {name}: Unable to convert to float")

# #     # Sort responses based on percentage match
# #     ranked_responses.sort(key=lambda x: x[2], reverse=True)
# #     return ranked_responses


# # Streamlit App
# st.set_page_config(page_title="Job suggestion by the resume analysis")
# st.header("Job Eligible prediction by resume analysis")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")
# # rank_button = st.button("Rank Resumes")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
# Please share your professional evaluation on whether the candidates' profiles align with the role. 
# Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resumes against the provided job description. 
# Give me the percentage of match if the resumes match the job description. 
# First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
# """

# if submit1:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt1, pdf_content, input_text, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# elif submit3:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt3, pdf_content, input_text, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# # elif rank_button:
# #     if uploaded_files:
# #         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
# #         responses = get_gemini_response(input_prompt3, pdf_content, input_text, candidate_names)
# #         ranked_responses = rank_resumes(responses)
# #         st.subheader("Ranked Resumes based on Percentage Match:")
# #         for i, (name, response) in enumerate(ranked_responses):
# #             st.write(f"Rank {i + 1}: Candidate {name}")
# #             st.write(response)
# #     else:
# #         st.write("Please upload at least one resume")









# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_text, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     responses = []
#     for pdf in pdf_content:
#         response = model.generate_content([input_text, pdf, prompt])
#         responses.append(response.text)
#     return responses

# def input_pdf_setup(uploaded_files):
#     pdf_parts = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Convert the PDF to image
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_part = {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#             pdf_parts.append(pdf_part)
#     return pdf_parts

# # Streamlit App
# st.set_page_config(page_title="Job suggestion by the resume analysis")
# st.header("Job Eligible prediction by resume analysis")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
# Please share your professional evaluation on whether the candidates' profiles align with the role. 
# Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resumes against the provided job description. 
# Give me the percentage of match if the resumes match the job description. 
# First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
# """

# if submit1:
#     if uploaded_files:
#         pdf_content = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The Responses are:")
#         for i, response in enumerate(responses):
#             st.write(f"Response for Resume {i + 1}:")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# elif submit3:
#     if uploaded_files:
#         pdf_content = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("The Responses are:")
#         for i, response in enumerate(responses):
#             st.write(f"Response for Resume {i + 1}:")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")












#code 2 gives the percentage of the each of the candidate with alignment






# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_text, pdf_content, prompt, candidate_names):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     responses = []
#     for name, pdf in zip(candidate_names, pdf_content):
#         response = model.generate_content([input_text, pdf, prompt])
#         responses.append((name, response.text))
#     return responses

# def input_pdf_setup(uploaded_files):
#     pdf_parts = []
#     candidate_names = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Extract candidate name from the file name
#             name = os.path.splitext(uploaded_file.name)[0]
#             candidate_names.append(name)

#             # Convert the PDF to image
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_part = {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#             pdf_parts.append(pdf_part)
#     return pdf_parts, candidate_names

# # Streamlit App
# st.set_page_config(page_title="Job suggestion by the resume analysis")
# st.header("Job Eligible prediction by resume analysis")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
# Please share your professional evaluation on whether the candidates' profiles align with the role. 
# Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resumes against the provided job description. 
# Give me the percentage of match if the resumes match the job description. 
# First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
# """

# if submit1:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_text, pdf_content, input_prompt1, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# elif submit3:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_text, pdf_content, input_prompt3, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")



















# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input_text, pdf_content, prompt, candidate_names):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     responses = []
#     for name, pdf in zip(candidate_names, pdf_content):
#         response = model.generate_content([input_text, pdf, prompt])
#         responses.append((name, response.text))
#     return responses

# def input_pdf_setup(uploaded_files):
#     pdf_parts = []
#     candidate_names = []
#     for uploaded_file in uploaded_files:
#         if uploaded_file is not None:
#             # Extract candidate name from the file name
#             name = os.path.splitext(uploaded_file.name)[0]
#             candidate_names.append(name)

#             # Convert the PDF to image
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_part = {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#             pdf_parts.append(pdf_part)
#     return pdf_parts, candidate_names

# # def rank_resumes(responses):
# #     ranked_responses = []
# #     for name, response in responses:
# #         try:
# #             # Extract percentage match from the response text
# #             match_line = response.split("\n")[0]
# #             if "Percentage match" in match_line:
# #                 percentage_match = match_line.split(":")[1].strip().strip("%")
# #                 percentage_match = float(percentage_match)
# #             else:
# #                 raise ValueError("Percentage match not found")
            
# #             ranked_responses.append((name, response, percentage_match))
# #         except IndexError:
# #             st.error(f"Error processing response for {name}: Index out of range")
# #         except ValueError:
# #             st.error(f"Error processing response for {name}: Unable to convert to float")

# #     # Sort responses based on percentage match
# #     ranked_responses.sort(key=lambda x: x[2], reverse=True)
# #     return ranked_responses


# # Streamlit App
# st.set_page_config(page_title="Job suggestion by the resume analysis")
# st.header("Job Eligible prediction by resume analysis")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_files = st.file_uploader("Upload your resume(PDF)...", type=["pdf"], accept_multiple_files=True)

# if uploaded_files:
#     st.write(f"{len(uploaded_files)} PDF(s) Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")
# # rank_button = st.button("Rank Resumes")

# input_prompt1 = """
# You are an experienced Technical Human Resource Manager, your task is to review the provided resumes against the job description. 
# Please share your professional evaluation on whether the candidates' profiles align with the role. 
# Highlight the strengths and weaknesses of the applicants in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
# Your task is to evaluate the resumes against the provided job description. 
# Give me the percentage of match if the resumes match the job description. 
# First, the output should come as a percentage, then keywords missing, and lastly final thoughts.
# """

# if submit1:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt1, pdf_content, input_text, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# elif submit3:
#     if uploaded_files:
#         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
#         responses = get_gemini_response(input_prompt3, pdf_content, input_text, candidate_names)
#         st.subheader("The Responses are:")
#         for name, response in responses:
#             st.write(f"Candidate: {name}")
#             st.write(response)
#     else:
#         st.write("Please upload at least one resume")

# # elif rank_button:
# #     if uploaded_files:
# #         pdf_content, candidate_names = input_pdf_setup(uploaded_files)
# #         responses = get_gemini_response(input_prompt3, pdf_content, input_text, candidate_names)
# #         ranked_responses = rank_resumes(responses)
# #         st.subheader("Ranked Resumes based on Percentage Match:")
# #         for i, (name, response) in enumerate(ranked_responses):
# #             st.write(f"Rank {i + 1}: Candidate {name}")
# #             st.write(response)
# #     else:
# #         st.write("Please upload at least one resume")

























