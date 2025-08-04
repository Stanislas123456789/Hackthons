import os
from cerebras.cloud.sdk import Cerebras

client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY", "csk-5hef36cn4ewpnxex2jxnkrn5vnkhtrcyyw9fth3r8emewnmp")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Why is fast inference important?",
        }
],
    model="llama-4-scout-17b-16e-instruct",
)

print(chat_completion)
