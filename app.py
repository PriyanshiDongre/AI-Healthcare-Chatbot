import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")


def healthcare_chatbot(user_input):
  if "symptom" in user_input:
    return "Please consult the doctor once"
  elif "appointment" in user_input:
    return "Do you need me to schedule an appointment for you" 
  elif "medication" in user_input:
    return "please take your medicines properly"
  else:
    response = chatbot(user_input,max_length=500,num_return_sequences=1)
    return response[0]['generated_text']


def main():
    st.title("Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today")
    if st.button("Clear"):
        user_input = ""

    if st.button("Submit"):
        if user_input:
             st.write("user: ",user_input)
             with st.spinner("Please wait...while we generate a response"):
              response = healthcare_chatbot(user_input)
             st.write("Healthcare assistant: ",response)
        else:
            st.write("Please enter accurate prompt")
          
main()