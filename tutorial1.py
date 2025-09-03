import openai

api_key = "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"

client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages = [
         {"role": "system", "content": "You are a grumpy assistant."},
        {"role": "user", "content": "Explain what is promt chaining?"}
    ],
    temperature=0.3,
    max_tokens=400
)

print(response.choices[0].message.content)
