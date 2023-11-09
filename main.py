import os
import openai
openai.api_type = "azure"
openai.api_base = "05da51ff63ed47f991ded3a2dccaff23" 
openai.api_key = "05da51ff63ed47f991ded3a2dccaff23"
openai.api_version = "2023-05-15"

response = openai.ChatCompletion.create(
    engine="salimmasl", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])