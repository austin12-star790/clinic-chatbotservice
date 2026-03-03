# 🦷 Dental AI Chatbot

AI-powered chatbot for dental clinics.
Provides 24/7 automated responses, appointment assistance, and FAQ handling.

---

## 🚀 Features

- AI-powered responses using OpenAI
- Website integration ready
- Telegram bot compatible
- Lead capture ready
- Easy deployment (Render / Railway)

---

## 📦 Installation

1. Clone repository
2. Create virtual environment

python -m venv venv
source venv/bin/activate  (Mac/Linux)
venv\Scripts\activate     (Windows)

3. Install dependencies

pip install -r requirements.txt

4. Create `.env` file and add your OpenAI key

5. Run server

python app.py

---

## 🌐 API Endpoint

POST /chat

Request:
{
  "message": "Hello"
}

Response:
{
  "reply": "Hello! How can I help you today?"
}

---

## 🏥 Example Use Cases

- Answer dental FAQs
- Explain procedures
- Provide clinic hours
- Help book appointments
- Capture patient leads

---

## 🔐 Security

Environment variables stored in `.env`
Never expose API keys publicly.

---

## 💼 Business Model

This chatbot can be:
- Sold as a service to dental clinics
- Integrated into clinic websites
- Offered as a monthly subscription

---

Built with ❤️ using Flask + OpenAI