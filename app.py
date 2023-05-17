from flask import Flask, render_template, request
import openai
from config import OPENAI_API_KEY
import io
import PyPDF2

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])

def process():
    # Get the uploaded PDF file from the form
    uploaded_file = request.files['pdf_file']

    # Create a BytesIO object and write the uploaded file content to it
    pdf_file = io.BytesIO()
    pdf_file.write(uploaded_file.read())

    # Seek to the beginning of the file
    pdf_file.seek(0)

    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract the text content from the PDF file
    text_content = ''
    for page in pdf_reader.pages:
        text_content += page.extract_text()

    # Close the BytesIO object
    pdf_file.close()

    # Generate the summary
    summary = summarize_text(text_content)

    # Pass the extracted text content and summary to the template for display
    return render_template('result.html', text_content=text_content, summary=summary)


def summarize_text(text_content):
    # Reduce the length of text_content
    shortened_text = text_content[:3000]  # Adjust the desired length

    # Make the API call with the shortened text
    # print("Making API call with text:", shortened_text)  # Print the shortened text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=shortened_text,
        max_tokens=500
    )

    # Extract the generated summary from the response
    summary = response.choices[0].text.strip()

    # print("Generated summary:", summary)  # Print the generated summary
    return summary



if __name__ == '__main__':
    app.run(port=5001)

