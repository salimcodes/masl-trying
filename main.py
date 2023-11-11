import openai
import re
import requests
import sys
import os
#import pandas as pd
#import numpy as np
#from dotenv import load_dotenv
#load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-05-15"

API_KEY = "0ac848ca2f0e4ea0a0a0b107886e09bd"
assert API_KEY, "ERROR: Azure OpenAI Key is missing"
openai.api_key = API_KEY

RESOURCE_ENDPOINT = "https://trying.openai.azure.com/"
assert RESOURCE_ENDPOINT, "ERROR: Azure OpenAI Endpoint is missing"
assert "openai.azure.com" in RESOURCE_ENDPOINT.lower(), "ERROR: Azure OpenAI Endpoint should be in the form: \n\n\t<your unique endpoint identifier>.openai.azure.com"
openai.api_base = RESOURCE_ENDPOINT


CHAT_COMPLETIONS_MODEL = 'masl-salim'
ourNote = input("Enter your note: ")
prompt = """I will input a rough note. I want you to return a very comprehensive version of the note with sections and everything in between translated to French, the Nigerian language".
Q: """ + ourNote + """
A:"""
response = openai.ChatCompletion.create(
  engine="masl-salim",
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},])

print(response['choices'][0]['message']['content'])