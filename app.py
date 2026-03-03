import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from models import add_appointment, get_appointments

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FAQ database (simple)
FAQ = {
    "hours": "We are open Monday–Friday, 9am–5pm.",
    "location": "123 Dental Street, Smile City.",
    "services": "We offer cleanings, fillings, checkups, and cosmetic dentistry.",
}

conversation = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant for a dental clinic. "
            "You can answer dental questions and help book appointments. "
            "If the user wants to book an appointment, ask for name, date, and service."
        ),
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    conversation.append({"role": "user", "content": user_message})

    # FAQ shortcut
    if user_message.lower() in FAQ:
        return jsonify({"response": FAQ[user_message.lower()]})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        answer = response.choices[0].message.content
        conversation.append({"role": "assistant", "content": answer})
        return jsonify({"response": answer})

    except Exception as e:
        return jsonify({"response": f"Error: {e}"})


@app.route("/book", methods=["POST"])
def book():
    data = request.json
    add_appointment(data["name"], data["date"], data["service"])
    return jsonify({"status": "Appointment booked!"})


@app.route("/appointments")
def appointments():
    return jsonify(get_appointments())


if __name__ == "__main__":
    app.run(debug=True)