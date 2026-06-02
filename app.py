import streamlit as st
import requests

##server_loc = st.secrets["SERVER_URL"]

with st.form("details"):
    st.title("AI INTERVIEW QUESTIONS CHAT BOT ")

    question = st.text_input("Enter your question")

    choice = st.selectbox(
        "choice option",
        ["EASY", "MEDIUM", "HARD"]
    )

    option = st.multiselect(
        "select",
        ["theory", "MCQS", "coding"]
    )

    st.write(option)

    if st.form_submit_button("submit"):

        prompt = f"""
        You are an expert AI interview preparation assistant.

        Generate interview questions based on the following details:

        Topic: {question}
        Difficulty Level: {choice}
        Question Type: {option}

        Instructions:
        1. If theory is selected, generate theoretical interview questions with answers.
        2. If MCQS is selected, generate multiple choice questions with 4 options and correct answers.
        3. If coding is selected, generate coding interview questions with solutions.
        4. Keep the response clean and well structured.
        5. Generate at least 5 questions.
        6. Difficulty must match the selected level.
        7. Questions should be suitable for technical interviews.
        """

        response = requests.post(
            f"{server_loc}/questions",
            json={"prompt": prompt}
        )

        result = response.json()

        st.write(result["response"])