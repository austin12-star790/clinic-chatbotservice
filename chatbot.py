import os
from openai import OpenAI

# Initialize OpenAI client using environment variable (recommended)
client = OpenAI(api_key=("your openai key-"))

print("🤖 Dental Clinic AI Chatbot is running. Type 'exit' to stop.\n")

# System prompt: defines chatbot role
system_prompt = {
    "role": "system",
    "content": (
        "You are a helpful AI assistant for a dental clinic. "
        "You answer questions about dental health, appointments, "
        "clinic services, and general patient guidance. "
        "Be friendly and professional."
    )
}

conversation = [system_prompt]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        answer = response.choices[0].message.content
        print("AI:", answer)

        conversation.append({"role": "assistant", "content": answer})

    except Exception as e:
        print("Error:", e)