import os
from openai import OpenAI

# Retrieve the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")
print("API Key:", api_key)  # Print the API key for debugging

# Create an OpenAI client instance
client = OpenAI(api_key=api_key)

# Create a completion using the OpenAI client
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)  # Print the completion for debugging




