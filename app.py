import os
import openai

#key = os.environ["AZURE_OPENAI_KEY"]
#endpoint =os.environ['AZURE_OPENAI_ENDPOINT']

openai.api_key = "05da51ff63ed47f991ded3a2dccaff23"
openai.api_base = "https://tryingopenai.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this might change in the future

deployment_name='salimmasl' #This will correspond to the custom name you chose for your deployment when you deployed a model. 

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Return a mail asking for a meeting with the client'
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(text)