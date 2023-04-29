import openai
openai.api_key="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"
def BasicGeneration(userPrompt):
    completion=openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user","content": userPrompt}])
    return completion.choices[0].message.content
prompt=input("Enter the Prompt:")
response=BasicGeneration(prompt)
print(response)