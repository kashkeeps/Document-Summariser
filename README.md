
# Document Summarizer

Document Summarizer is a project that leverages OpenAI's language model to generate summaries of text documents. It utilizes the OpenAI GPT-3.5 model for text completion to condense lengthy documents into shorter, more concise summaries.

## Features

- Summarize text documents: Given a text document, the project generates a summary using the OpenAI GPT-3.5 language model.
- Easy-to-use API integration: The project provides an API endpoint that can be used to send requests and receive summary responses.
- Rate limit management: The project implements rate limit handling to ensure compliance with OpenAI's API rate limits.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/document-summarizer.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up OpenAI API credentials:
   - Obtain an API key from OpenAI.
   - Set the `OPENAI_API_KEY` environment variable to your API key.

4. Run the application:

```
python app.py
```

## Usage

Once the application is running, you can send HTTP POST requests to the `/process` endpoint to summarize text documents. The documents should be included in the request body.

Example using cURL:

```
curl -X POST -H "Content-Type: application/json" -d '{"text": "Your text document goes here."}' http://localhost:5000/process
```

The response will contain the generated summary.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Disclaimer

This project utilizes the OpenAI GPT-3.5 model and is subject to OpenAI's usage policies and rate limits. Make sure to comply with OpenAI's terms of service when using the project.

## Acknowledgements

This project was inspired by the capabilities of OpenAI's language models and the need for document summarization in various applications.


