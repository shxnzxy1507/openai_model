import os
from openai import OpenAI

# Retrieve the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Verify that the API key is not None or empty
if not api_key:
    raise ValueError("API key not found in environment variables")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Create a chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

# Print the chat completion message
print(completion.choices[0].message)


