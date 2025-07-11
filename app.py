import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

# Set up Flask
app = Flask(__name__)

# Get Gemini API Key from .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    input_text = request.form.get("text")
    if not input_text:
        return "Please enter some text to summarize."
    try:
        response = model.generate_content(f"Summarize this:\n{input_text}")
        summary = response.text
    except Exception as e:
        summary = f"Error: {str(e)}"
    return render_template("result.html", original=input_text, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
