import streamlit as st
import pandas as pd
import numpy as np
import openai
from googletrans import Translator

#title
st.title('GPTHero')
#description
st.write('GPTHero attempts to make ai-generated text appear more human. It has the same capabilities as the latest and greatest -- just with the propensity to write poorly. Feel free to check the output against the GPTZero AI detector to see if it is human or not.')
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7,
    )
    return response['choices'][0]['text']
#user input for the api key, set a variable on submit. after submit, hide the input
api_key = st.text_input("Enter your OpenAI API key")
if st.button('Submit'):
  st.write('API key set!')
  openai.api_key = api_key
#user input
user_input = st.text_input("Enter your text request")

#button
if st.button('Generate'):
    st.write('Generating...')
    #call openai on the prompt
    output = generate_text(user_input)
    prompt = """Start of English Text:
INPUT0

Start of Swahili Translation:"""
    prompt = prompt.replace("INPUT0", output)
    #call openai on the prompt
    output = generate_text(prompt)
    #display that it is halfway done
    st.write('Finished step 1...')
    prompt = """Start of Swahili Text:
INPUT0

Start of French Translation:"""
    prompt = prompt.replace("INPUT0", output)
    #call openai on the prompt
    output = generate_text(prompt)
    #display that it is halfway done
    st.write('Finished step 2...')

    #translate to english
    translator = Translator()
    output = translator.translate(output, dest='en')
    final = output.text
    #replace periods with a period and a space
    final = final.replace(".", ". ")
    #display output
    st.write(final)


