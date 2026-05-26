# Cyberlihle Project
This project is a Flask-based AI chatbot that utilizes OpenAI for generating human-like responses.
## Description
The Cyberlihle project is designed to provide a conversational interface for users to interact with a chatbot. The chatbot uses OpenAI's text-davinci-003 engine to generate responses to user queries.
## Key Features
- Utilizes OpenAI's text-davinci-003 engine for generating human-like responses
- Supports caching for storing chat history
- Handles user input and generates responses accordingly
## Tech Stack
- Flask: Web framework for building the chatbot
- OpenAI: AI engine for generating human-like responses
- Flask-Caching: Library for caching chat history
## Installation
To install the project, follow these steps:
1. Clone the repository: git clone https://github.com/your-username/Cyberlihle.git
2. Install dependencies: pip install -r requirements.txt
3. Set environment variables: API_KEY (OpenAI API key)
## Usage
To run the chatbot, follow these steps:
1. Run the Flask app: flask run
2. Send a POST request to the /webhook endpoint with a JSON payload containing the user's query
## Environment Variables
- API_KEY: OpenAI API key
- CACHE_TYPE: Cache type (default: simple)
- CACHE_DEFAULT_TIMEOUT: Cache timeout (default: 1800)
## Code
```

from flask import Flask, request, jsonify
import traceback
import random
import openai
import os
from dotenv import load_dotenv
from flask_caching import Cache
import uuid

```

## Example Use Case
To test the chatbot, send a POST request to the /webhook endpoint with a JSON payload containing the user's query. For example:
```

{
  "queryResult": {
    "queryText": "Hello, how are you?"
  }
}

```