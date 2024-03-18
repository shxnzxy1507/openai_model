from openai import OpenAI

# Initialize the OpenAI client with organization ID
client = OpenAI(
    organization='org-2LzSNGf8ab5RCjWbDm0hy5fg'
)

# Now you can use the OpenAI client for making requests
# For example:
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)



