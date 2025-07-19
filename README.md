# ✨ Document Summarizer

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-Backend-lightgrey?logo=flask" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/Gemini%20AI-API-blueviolet?logo=google&logoColor=white" alt="Gemini AI Badge"/>
  <img src="https://img.shields.io/badge/HTML-Frontend-orange?logo=html5&logoColor=white" alt="HTML Badge"/>
  <img src="https://img.shields.io/badge/CSS-Styling-blue?logo=css3&logoColor=white" alt="CSS Badge"/>
  <img src="https://img.shields.io/badge/Git-VersionControl-orange?logo=git&logoColor=white" alt="Git Badge"/>
  <img src="https://img.shields.io/badge/Status-Learning_Project-blue" alt="Status Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge"/>
</p>

> An AI-powered web application that generates concise summaries of long documents using Google’s **Gemini 1.5 Flash model**.  
> Built during my personal exploration of Generative AI, NLP, and backend development.

---

## 🔍 Features

- 📄 Summarizes long-form text into concise content
- ⚡ Fast and responsive Flask-based web interface
- 🧠 Uses Gemini AI API for high-quality summaries
- 🖥️ Clean, minimal frontend with HTML and CSS
- 🛠️ Simple, beginner-friendly codebase

---

## 🛠️ Tech Stack

| Component   | Technology                      |
|-------------|----------------------------------|
| Language    | Python                           |
| Backend     | Flask                            |
| AI Model    | Gemini 1.5 Flash (Google GenAI)  |
| Frontend    | HTML, CSS                        |
| Tools       | Git, GitHub, VS Code             |

---

## 🚀 Getting Started

1. **Clone the repository**

```bash
   git clone https://github.com/yourusername/document-summarizer.git
   cd document-summarizer
```
2. **Install dependencies**
   
```bash
  pip install -r requirements.txt

```
3. **Add your Gemini API key**

In app.py, configure the Gemini API:

```python
genai.configure(api_key="your-api-key-here")
```

4. **Run the app**

```bash
python app.py
```

5. **Open in browser**

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000/)

---

## 📁 Project Structure

```csharp
document-summariser/
├── app/
│   ├── routes.py           # Flask routes and Gemini summarization logic
│   └── templates/
│       ├── index.html      # Homepage
│       └── result.html     # Summary display
├── static/
│   └── style.css           # Optional styling
├── .env                    # API key (not uploaded)
├── .gitignore
├── Procfile                # For deployment
├── requirements.txt
├── app.py                  # Entry point (or use routes.py inside /app)
├── README.md

```

---

## 🌱 Why I Built This

This project is part of my personal learning journey in:

- 🔹Integrating Generative AI into real-world apps
- 🔹Understanding backend frameworks like Flask
- 🔹Practicing API usage and UI logic
- 🔹Exploring the capabilities of Gemini AI for NLP

---

## 🔮 Future Enhancements

- 📥 Upload support for .txt, .pdf, or .docx files
- 🌍 Multi-language support
- 💾 Option to save or download summaries
- 🔐 Login system with summary history
- 🌐 Deploy to Firebase or Render

---

## 🙋‍♀️ Made by

Kashish Aggarwal
- Aspiring Full Stack Developer
- [GitHub](https://github.com/kashkeeps) • [LinkedIn](https://www.linkedin.com/in/kashish-aggarwal-a389b7203/)


