from openai import OpenAI

# Set your OpenAI API key here
api_key = "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"

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
